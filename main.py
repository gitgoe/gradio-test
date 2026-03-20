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

warnings.filterwarnings("ignore", category=FutureWarning, module="seaborn")

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

load_json_data()

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
