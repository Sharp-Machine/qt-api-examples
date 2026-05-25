# qt-api-examples

This repository provides minimal, zero-setup examples demonstrating how to use the Quantile Transformer (QT) Engine API. The QT Engine is a real-time Physical AI that predicts continuous, multidimensional structural uncertainty.

These examples use standard HTTP requests to communicate with the asynchronous cloud API, ensuring that you can easily integrate QT probability forecasting into your existing robotics or quantitative finance stack.

## Examples Provided

- **Robotics (7 DOF):** `generate_robotics.js` - A Node.js example showing how to fetch 100 conditional future trajectories for a 7-DOF robotic arm.
- **Finance (Tabular):** `generate_tabular.py` - A Python example showing how to fetch future paths conditioned on tabular features.

## Usage

You will need a valid API key. A free tier demo key (`AIzaSyDAVGM-E3WIjd4PAJnErxSDzb-sXYIZdE8`) is hardcoded in the examples for quick testing.

### Python
```bash
pip install requests
python generate_tabular.py
```

### Node.js
```bash
node generate_robotics.js
```

## Need a Native SDK?
If you are working in Python, we recommend using our native SDK which abstracts away the HTTP polling entirely:
```bash
pip install qt-client
```
