<div align="center">
  <img src="robotics_plot.png" alt="QT Structural Uncertainty Prediction" width="800"/>
  <h1>Quantile Transformer (QT) Engine</h1>
  <p><strong>Zero-Setup API Examples for Continuous Physical AI</strong></p>
</div>

---

The Quantile Transformer (QT) Engine is a real-time Physical AI that predicts continuous, multidimensional structural uncertainty. 

This repository provides zero-friction "Sandboxes" that allow you to generate 100 conditional future trajectories in **under 60 seconds**, without installing any neural network weights or managing GPUs. The heavy latent-space transformations execute securely via our asynchronous Cloud API.

## 🚀 The "WOW" Sandboxes

Choose your preferred environment to instantly visualize the power of QT:

### 1. The Browser Sandbox (Web/JS)
Double-click `index.html` to open it in your browser. No `npm install`, no build steps. It instantly uses Plotly.js to render 100 conditional robotics trajectories directly in your browser.

### 2. The Notebook Sandbox (Data Science)
Open `quickstart.ipynb` in Jupyter or VSCode. This notebook uses a beautiful dark-mode `matplotlib` theme to plot the confidence intervals and physical trajectories.

## 💻 Raw API Scripts
If you just want the raw HTTP polling logic to integrate into your backend:
- **Python:** `generate_tabular.py`
- **Node.js:** `generate_robotics.js`

*(Note: These examples use a hardcoded free-tier API key `AIzaSyDAVGM-E3WIjd4PAJnErxSDzb-sXYIZdE8` for instant testing).*

## 📦 Need a Native SDK?
If you are working in Python, we recommend using our native SDK which abstracts away the HTTP polling entirely:
```bash
pip install qt-client
```
