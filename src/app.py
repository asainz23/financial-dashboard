import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Financial Screener", layout="wide")

st.title("📈 Financial Market Data Screener")
st.markdown("""
This app performs basic technical analysis on stocks using data from Yahoo Finance.
It calculates the **20-day SMA** and **Logarithmic Returns**.
""")

# --- SIDEBAR - USER INPUTS ---
st.sidebar.header("User Input Parameters")

# Let the user type any ticker
ticker_symbol = st.sidebar.text_input("Enter Ticker Symbol", value="SAN.MC")

# Let the user choose the time period
period = st.sidebar.selectbox("Select Period", options=["6mo", "1y", "2y", "5y"], index=1)

# --- DATA FETCHING ---
@st.cache_data # This decorator saves time by not re-downloading data if inputs don't change
def load_data(ticker, time_period):
    data = yf.download(ticker, period=time_period, auto_adjust=True)
    return data

try:
    df = load_data(ticker_symbol, period)

    if df.empty:
        st.error("No data found. Please check the Ticker Symbol.")
    else:
        # --- QUANTITATIVE CALCULATIONS ---
        df['SMA_20'] = df['Close'].rolling(window=20).mean()
        df['Log_Return'] = np.log(df['Close']).diff()
        df_clean = df.dropna()

        # --- LAYOUT: TWO COLUMNS ---
        col1, col2 = st.columns(2)

        with col1:
            st.subheader(f"Price vs Trend (SMA 20) - {ticker_symbol}")
            fig1, ax1 = plt.subplots(figsize=(10, 5))
            ax1.plot(df_clean.index, df_clean['Close'], label='Close Price', color='black', alpha=0.6)
            ax1.plot(df_clean.index, df_clean['SMA_20'], label='SMA 20', color='red')
            ax1.legend()
            ax1.grid(True, alpha=0.3)
            st.pyplot(fig1)

        with col2:
            st.subheader("Daily Returns Distribution (Risk)")
            fig2, ax2 = plt.subplots(figsize=(10, 5))
            ax2.hist(df_clean['Log_Return'], bins=40, color='royalblue', edgecolor='black', alpha=0.7)
            ax2.axvline(0, color='red', linestyle='--')
            st.pyplot(fig2)

        # --- DATA TABLE ---
        st.subheader("Recent Market Data")
        st.dataframe(df_clean.tail(10), width='stretch')

except Exception as e:
    st.write("Please enter a valid ticker to start.")