import sys
import os

# Add the local package to python path for testing (in a real scenario, this would be pip installed)
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "qt-client"))

from qt_client import QTClient

def main():
    print("Initialize QT Client...")
    # Abstracted polling handled by the SDK
    client = QTClient(base_url="http://localhost:8000")

    # In a real environment, load the model into memory first
    import requests
    import os
    model_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "temp_models", "droid_v1.pkl"))
    requests.post(f"http://localhost:8000/models/nonlinear/load", params={"path": model_path})

    print("Requesting 100 trajectories from QT Engine (Non-linear)...")
    
    # We pass prefix=None to simulate an unconditional generation from the default model center
    trajectories = client.generate(
        model_id="nonlinear",
        modality="robotics_7dof",
        n_samples=100,
        prefix=None 
    )

    print("\nGeneration Complete!")
    print(f"Received numpy array of shape: {trajectories.shape}")
    print(f"Sample 0, Timestep 0 (Base Joint): {trajectories[0][0]:.4f}")

if __name__ == "__main__":
    main()
