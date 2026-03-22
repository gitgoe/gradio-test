import gradio as gr
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import warnings
import os
import tempfile
from cachetools import cached, TTLCache
import json
from json import dumps
import requests

warnings.filterwarnings("ignore", category=FutureWarning, module="seaborn")

def call_web_service(endpoint, api_key=None, data=None):
    """
    Call a secure web service and return the response

    Args:
        endpoint (str): The HTTPS URL of the web service
        api_key (str, optional): API key for authentication
        data (dict, optional): Data to send in the request body

    Returns:
        str: Response from the web service or error message
    """
    try:
        # Prepare headers
        headers = {
            'Content-Type': 'application/json',
            'User-Agent': 'Gradio-Web-Client/1.0'
        }

        # Add authentication if API key provided
        if api_key:
            headers['Authorization'] = f'Bearer {api_key}'
            # Alternative: headers['X-API-Key'] = api_key

        # Make the HTTP request
        if data:
            # POST request with data
            response = requests.post(
                endpoint,
                headers=headers,
                json=data,
                timeout=30,
                verify=True  # Verify SSL certificate (secure)
            )
        else:
            # GET request
            response = requests.get(
                endpoint,
                headers=headers,
                timeout=30,
                verify=True  # Verify SSL certificate (secure)
            )

        # Check if request was successful
        if response.status_code == 200:
            try:
                return json.dumps(response.json(), indent=2)
            except:
                return response.text
        else:
            return f"Error {response.status_code}: {response.text}"

    except requests.exceptions.SSLError:
        return "SSL Error: The service's SSL certificate is not valid"
    except requests.exceptions.Timeout:
        return "Timeout: The request took too long to complete"
    except requests.exceptions.ConnectionError:
        return "Connection Error: Could not connect to the service"
    except Exception as e:
        return f"Error: {str(e)}"

# ------------------------------------------------------------------
# 1) Load CSV data once
# ------------------------------------------------------------------
json_data = None


def load_json_data():
    global json_data
    with open("./data/batch.json", 'r') as f:
        raw_json_data = json.load(f)['data']
        json_attributes = [item['attributes'] for item in raw_json_data]
        print(json_attributes[0])
        json_data = pd.json_normalize(json_attributes)
        json_data = json_data.drop(columns=['applicationOD','applicationGroupOD','streamWeaverScriptName','indexKey','refDocList','streamWeaverEngine','serviceName','docType','nbrOfCopies','dialogueEngine','recipients'])
        json_data.insert(len(json_data.columns), 'selected', False)
        print(json_data)
def load_json_data_ws():
    global json_data
    try:
        json_string =  call_web_service("http://127.0.0.1:8000/", "")
        raw_json_data = json.loads(json_string)['data']
        print(raw_json_data)
        json_attributes = [item['attributes'] for item in raw_json_data]
        print(json_attributes[0])
        json_data = pd.json_normalize(json_attributes)
        json_data = json_data.drop(
            columns=['applicationOD', 'applicationGroupOD', 'streamWeaverScriptName', 'indexKey', 'refDocList',
                     'streamWeaverEngine', 'serviceName', 'docType', 'nbrOfCopies', 'dialogueEngine', 'recipients'])
        json_data.insert(len(json_data.columns), 'selected', False)
    except json.JSONDecodeError as e:
        print('Error:', e)
        print('The JSON string is not properly formatted')


# load_json_data()
load_json_data_ws()

cache = TTLCache(maxsize=128, ttl=300)

def get_date_range():
    global json_data
    if json_data is None or json_data.empty:
        return None, None
    return json_data['creationDateTime'].min(), json_data['creationDateTime'].max()

def update_dashboard(start_date, end_date):
    table_data = json_data
    return (table_data)


def get_selected_rows(df: pd.DataFrame):
    if df is None or df.empty:
        return pd.DataFrame()
    # Expecting a boolean "Select" column
    mask = df["selected"] == True
    selected = df.loc[mask, df.columns[df.columns != "selected"]]
    # You can also return list of IDs if you prefer:
    #return df.loc[mask, "timeStamp"].tolist()
    return selected.reset_index(drop=True)

def create_dashboard():
    min_date, max_date = get_date_range()
    if min_date is None or max_date is None:
        min_date = datetime.datetime.now()
        max_date = datetime.datetime.now()

    default_start_date = min_date
    default_end_date = max_date

    with gr.Blocks() as dashboard:

        gr.Markdown("# Impressions Dashboard")

        # Filters row
        with gr.Row():
            start_date = gr.DateTime(
                label="Start Date",
                value=default_start_date,
                include_time=False,
                type="datetime"
            )
            end_date = gr.DateTime(
                label="End Date",
                value=default_end_date,
                include_time=False,
                type="datetime"
            )

        gr.Markdown("# Traitements")
        # Data Table (below the plots)
        data_table = gr.DataFrame(
            label="list des jobs",
            type="pandas",
            value=json_data,
            interactive=True,
            datatype=["str", "str","str", "str","str", "str","str", "bool"]
        )


        refresh_btn = gr.Button('🔄 Refresh Data', variant='primary')
        refresh_btn.click(
            fn=load_json_data_ws(),
            outputs=[data_table]
        )

        btn = gr.Button("Get selected")
        out = gr.Dataframe(label="Selected rows", interactive=False)

        btn.click(get_selected_rows, inputs=data_table, outputs=out)

        # Initial load
        dashboard.load(
            fn=lambda: update_dashboard(default_start_date, default_end_date),
            outputs=[
                data_table
            ]
        )

    return dashboard

if __name__ == "__main__":
    css = """
               footer {display: none !important;}
               .tabs {border: none !important;}  
               .gr-plot {border: none !important; box-shadow: none !important;}
           """

    dashboard = create_dashboard()
    dashboard.launch(share=False, css=css)
