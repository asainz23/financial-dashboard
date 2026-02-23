# Financial Screener Pro

Automated market analysis for real-time stock insights. This dashboard handles data ingestion, quantitative normalization, trend identification, and risk profiling to return clean-language insights plus interactive visualizations.

## Why it matters

* **Accessibility:** Translates raw market data into concise, easy-to-read financial summaries.
* **Accuracy:** Uses logarithmic returns and SMA filters to avoid skewed performance data.
* **Speed:** Orchestrates yfinance + Streamlit stages so analysts get guidance within seconds.

## Architecture at a glance

* **Frontend (Streamlit):** Handles user inputs (tickers/periods) and renders interactive price charts and risk distributions.
* **Logic (Pandas/NumPy):** Performs vectorized operations for Logarithmic Returns and Moving Average (SMA) calculations.
* **Data Layer (yfinance):** Connects to Yahoo Finance API for real-time and historical price data extraction.
* **Environment:** Isolated Python venv to ensure consistent dependency management and reproducibility.

## Repository layout

* `notebooks/` — Research & Development lab. Contains experimental data extraction and plotting.
* `src/` — Production-ready code. Contains the main Streamlit application logic.
* `.gitignore` — Template for environment variables and ignored Python cache files.
* `requirements.txt` — Project dependencies (Pandas, yfinance, Streamlit).

## Getting started

### Prerequisites

* Python 3.11+ and PowerShell (Windows users).
* Basic understanding of financial tickers (e.g., AAPL, SAN.MC).

### Backend setup

1. Create a virtual environment and install dependencies:

   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate
   pip install pandas yfinance streamlit