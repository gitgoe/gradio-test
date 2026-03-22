import gradio as gr
import requests
import json


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


# Create Gradio interface
def create_interface():
    with gr.Blocks(title="Secure Web Service Client") as demo:
        gr.Markdown("# 🔒 Secure Web Service Client")
        gr.Markdown("Call HTTPS web services with authentication")

        with gr.Row():
            with gr.Column():
                endpoint = gr.Textbox(
                    label="Service Endpoint (HTTPS URL)",
                    placeholder="https://api.example.com/endpoint",
                    value="https://httpbin.org/get"  # Test endpoint
                )
                api_key = gr.Textbox(
                    label="API Key (optional)",
                    placeholder="Enter your API key",
                    type="password"
                )

                with gr.Row():
                    get_btn = gr.Button("GET Request", variant="primary")
                    post_btn = gr.Button("POST Request", variant="secondary")

                # Example JSON data for POST requests
                json_data = gr.Textbox(
                    label="JSON Data (for POST requests)",
                    placeholder='{"key": "value"}',
                    lines=3,
                    value='{"name": "Gradio", "action": "test"}'
                )

            with gr.Column():
                response_output = gr.Textbox(
                    label="Response",
                    lines=20,
                    max_lines=30
                )

        # Define button actions
        get_btn.click(
            fn=lambda endpoint, api_key: call_web_service(endpoint, api_key),
            inputs=[endpoint, api_key],
            outputs=response_output
        )

        post_btn.click(
            fn=lambda endpoint, api_key, data: call_web_service(endpoint, api_key, json.loads(data) if data else None),
            inputs=[endpoint, api_key, json_data],
            outputs=response_output
        )

    return demo


# Run the app
if __name__ == "__main__":
    app = create_interface()
    app.launch()
