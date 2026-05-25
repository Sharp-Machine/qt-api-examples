import time
import requests
import json
import sys

# Replace with your actual API key
API_KEY = "AIzaSyDAVGM-E3WIjd4PAJnErxSDzb-sXYIZdE8"

# The public Gateway URL
BASE_URL = "https://qt-paas-gateway-ane34s9g.uc.gateway.dev"

def generate_tabular_data():
    """
    Demonstrates how to use the QT API to predict Continuous Quantile trajectories 
    for Tabular/Financial data using an asynchronous polling loop.
    """
    print("Initiating Tabular/Financial Future Generation via QT API...")
    
    # 1. Define the payload for the Tabular Modality
    payload = {
        "type": "finance_tabular",
        "model_id": "engine",  # The backend routes to the correct tabular model automatically
        "features": [0.5, 0.2, -0.1, 0.9, 0.05], # Example conditional features (e.g. market indicators)
        "n_samples": 100       # How many distinct probability paths to generate
    }

    headers = {
        "Content-Type": "application/json",
        "X-QT-Api-Key": "qt_demo_123"  # Required header for this specific demo backend
    }

    # 2. Fire the initial POST request to the Gateway
    try:
        init_response = requests.post(
            f"{BASE_URL}/generate?key={API_KEY}", 
            json=payload, 
            headers=headers
        )
        init_response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Failed to initiate generation: {e}")
        sys.exit(1)

    init_data = init_response.json()
    operation_id = init_data.get("operation_id")
    
    print(f"Success! Generation accepted. Operation ID: {operation_id}")
    print("Polling for results (this usually takes 1-3 seconds)...")

    # 3. Poll the server until the generative inference is complete
    is_done = False
    result_data = None
    
    while not is_done:
        time.sleep(1) # Poll every 1 second
        try:
            poll_response = requests.get(
                f"{BASE_URL}/operations/{operation_id}?key={API_KEY}",
                headers=headers
            )
            poll_response.raise_for_status()
            poll_data = poll_response.json()
            
            if poll_data.get("done"):
                is_done = True
                result_data = poll_data.get("response")
                print("\n[SUCCESS] Generation Complete!")
            else:
                sys.stdout.write(".")
                sys.stdout.flush()
                
        except requests.exceptions.RequestException as e:
            print(f"\nError while polling: {e}")
            sys.exit(1)

    # 4. Process the returned distributions
    samples = result_data.get("samples")
    latency = result_data.get("inference_latency_ms")
    
    print(f"\nReceived {len(samples)} distinct future paths.")
    print(f"Each path contains {len(samples[0])} continuous dimensional states.")
    print(f"Server-side Inference Latency: {latency:.2f} ms")
    
    # Example: Print the first 3 predicted steps of the first sample
    print("\nSample 1 (First 3 steps):")
    print(samples[0][:3])

if __name__ == "__main__":
    generate_tabular_data()
