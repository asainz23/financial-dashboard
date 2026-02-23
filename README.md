# Financial Market Data Screener & Dashboard

An automated tool designed for real-time market analysis, technical indicator calculation, and risk visualization. This project bridges the gap between raw financial data and actionable insights through a clean, interactive web interface.

## Why it matters

* **Accessibility:** Allows users to monitor any publicly traded asset available on Yahoo Finance through an intuitive UI.
* **Accuracy:** Focuses on Logarithmic Returns ($r = \ln(P_t / P_{t-1})$) to ensure mathematical consistency and time-additivity in risk profiling.
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

## Getting started

### Prerequisites

* Python 3.12+ and PowerShell (Windows recommended).
* Basic understanding of financial tickers and market periods.

### Application setup

1. Create a virtual environment and install dependencies:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\activate
   pip install pandas yfinance streamlit matplotlib numpy
   ```

2. Run the application:

   ```powershell
   streamlit run src/app.py
   ```

## Roadmap

- [ ] Add RSI (Relative Strength Index) calculation for overbought/oversold signals.
- [ ] Implement Monte Carlo simulations for future price forecasting.
- [ ] Export automated analysis reports to PDF or Excel.

---
**Author:** Alejandro Sainz Muñoz – *Business Analytics Student*