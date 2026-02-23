📈 Financial Market Data Screener & Dashboard
An automated tool designed for real-time market analysis, technical indicator calculation, and risk visualization. This project bridges the gap between raw financial data and actionable insights through a clean, interactive web interface.

🚀 Project Overview
This dashboard allows users to monitor any publicly traded asset available on Yahoo Finance. It focuses on two core pillars of financial analysis:Trend Identification: Using Moving Averages (SMA 20) to filter market noise and identify short-term momentum.Risk Profiling: Utilizing Logarithmic Returns to analyze price distribution and volatility—a standard practice in quantitative finance for its time-additivity properties.

🛠️ Tech StackLanguage: Python 3.12+Data Source: yfinance (Real-time market API)
Data Manipulation: Pandas & NumPy (Vectorized financial operations)
Visualization: Matplotlib (Static analysis) & Streamlit (Interactive UI)
Environment Management: Python Venv

📂 Project Structure
Plaintextfinancial-dashboard/
├── .venv/                # Isolated virtual environment
├── notebooks/            # Research & Development (Jupyter Notebooks)
│   └── 01_data_extraction.ipynb
├── src/                  # Production-ready source code
│   └── app.py            # Streamlit Web Application
├── .gitignore            # Ensures clean version control
└── README.md             # Project documentation

⚙️ Key Features
Dynamic Ticker Search: Instantly fetch data for any global ticker (e.g., SAN.MC, AAPL, BTC-USD).Quant Logic: Implementation of Logarithmic Returns ($r = \ln(P_t / P_{t-1})$) for more accurate statistical modeling.Interactive Controls: User-defined time horizons (6 months to 5 years) via a sidebar interface.Automated Cleaning: Built-in handling of dividends, stock splits, and missing data points (NaN handling).

📥 Installation & Usage
Clone the repository:Bashgit clone https://github.com/YOUR_USERNAME/financial-dashboard.git
cd financial-dashboard
Activate the environment:Bash# Windows
.\.venv\Scripts\activate
Run the application:Bashstreamlit run src/app.py
📈 Roadmap
[ ] Add RSI (Relative Strength Index) calculation.[ ] Implement Monte Carlo simulations for price forecasting.[ ] Export analysis reports to PDF/Excel.

Author: [Alejandro Sainz Muñoz] – Business Analytics Student