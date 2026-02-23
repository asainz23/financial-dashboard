# Financial Market Data Screener & Dashboard

An automated tool designed for real-time market analysis, technical indicator calculation, and risk visualization. This project bridges the gap between raw financial data and actionable insights through a clean, interactive web interface.

## Why it matters

* **Accessibility:** Allows users to monitor any publicly traded asset available on Yahoo Finance through an intuitive UI.
* **Accuracy:** Focuses on Logarithmic Returns to ensure mathematical consistency and time-additivity in risk profiling.
* **Trend Insight:** Leverages Moving Averages (SMA 20) to effectively filter market noise and identify short-term momentum.

## Architecture at a glance

* **Frontend (Streamlit):** Interactive dashboard featuring user-defined time horizons (6mo to 5y) and dynamic ticker search (e.g., `SAN.MC`, `AAPL`).
* **Logic (Pandas & NumPy):** Vectorized financial pipeline for indicator calculation and automated data cleaning (handling of splits, dividends, and NaNs).
* **Visualization (Matplotlib):** Renders high-fidelity trend charts and frequency distributions for volatility analysis.
* **Environment (Python Venv):** Isolated system using Python 3.12+ to ensure dependency stability and reproducibility.

## Repository layout

* `notebooks/` — Research & Development environment containing experimental data extraction and plotting.
* `src/` — Production-ready source code. Includes the main `app.py` for the Streamlit web application.
* `.gitignore` — Configuration to ensure clean version control by excluding environments and cache.
* `README.md` — Technical documentation and project setup guide.

## How to run the dashboard

### 1. Prerequisites
* Python 3.12+ and PowerShell (Windows recommended).
* Git installed on your system.

### 2. Setup and Installation
First, clone the repository and set up your isolated environment to avoid dependency conflicts:

```powershell
git clone [https://github.com/asainz23/financial-dashboard.git](https://github.com/asainz23/financial-dashboard.git)

cd financial-dashboard
python -m venv .venv
.\.venv\Scripts\activate

pip install pandas yfinance streamlit matplotlib numpy
```

### 3. Launching the Web App
With your virtual environment active (you should see `(.venv)` in your terminal prompt), start the Streamlit server by running:

```powershell
streamlit run src/app.py
```

### 4. Accessing the UI
Once the server is running, the dashboard will automatically open in your default web browser. If it doesn't, you can manually connect by navigating to this address in your browser:
* **Local URL:** `http://localhost:8501`

*(To stop the server at any time, simply press `Ctrl + C` in your terminal).*

## Roadmap

- [ ] Add RSI (Relative Strength Index) calculation for overbought/oversold signals.
- [ ] Implement Monte Carlo simulations for future price forecasting.
- [ ] Export automated analysis reports to PDF or Excel.

---
**Author:** Alejandro Sainz Muñoz – *Business Analytics Student*
