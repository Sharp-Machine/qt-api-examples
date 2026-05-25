import requests
import time
import json

BASE_URL = "http://localhost:8000"

def generate_trajectory_raw():
    """
    Demonstrates how to interact with the QT API using raw HTTP requests,
    without using the pip SDK. Useful for clients in other languages.
    """
    print("1. Loading Model...")
    import os
    model_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "temp_models", "droid_v1.pkl"))
    requests.post(f"{BASE_URL}/models/nonlinear/load", params={"path": model_path})

    print("2. Initiating Generation Request...")
    
    payload = {
        "type": "robotics_7dof",
        "model_id": "nonlinear",
        "n_samples": 5, # Just requesting 5 for brevity
        "prefix": [0.0, -0.78, 1.57] # Base, Shoulder, Elbow
    }
    
    init_res = requests.post(f"{BASE_URL}/generate", json=payload)
    init_res.raise_for_status()
    
    op_id = init_res.json()["operation_id"]
    print(f"-> Received Operation ID: {op_id}")
    
    print("\n2. Polling for results...")
    while True:
        poll_res = requests.get(f"{BASE_URL}/operations/{op_id}")
        poll_res.raise_for_status()
        data = poll_res.json()
        
        if data["done"]:
            if data["status"] == "FAILED":
                print(f"Error: {data['error']}")
                return
                
            print(f"-> Generation Complete in {data['response']['inference_latency_ms']:.2f}ms!")
            samples = data['response']['samples']
            print(f"-> Unpacked {len(samples)} trajectory paths.")
            break
            
        print("   Status: IN_PROGRESS... waiting 500ms")
        time.sleep(0.5)

if __name__ == "__main__":
    generate_trajectory_raw()
