import streamlit as st
import pandas as pd
from pandas_datareader import data as wb
import numpy as np
import datetime

st.write("""
# Is this stock still more profitable than the stock index?
""")

tickerSymbol = st.text_input('Company''s Ticket on Yahoo Finance (like FB, AMZN, MSFT, XP)', 'AMZN')

tickerBuyDate = st.date_input('Buy date yyyy-mm-dd', datetime.date(2020, 1, 1))

tickers = [tickerSymbol, '^IXIC', '^GSPC']
dataFrame = pd.DataFrame()
for t in tickers:
    dataFrame[t] = wb.DataReader(t, data_source='yahoo', start=tickerBuyDate)['Adj Close']


st.line_chart((dataFrame/dataFrame.iloc[0]*100))


st.write("""
# Esta ação está se mantendo mais lucrativa que o indice da bolsa? 
""")

tickerSymbol = st.text_input('Código da Empresa no Yahoo Finance (ex.: LREN3.SA, EGIE3.SA, ITSA4.SA, WEGE3.SA, MGLU3.SA, TRIS3.SA)', 'LREN3.SA')

tickerBuyDate = st.date_input('Data de Compra aaaa-mm-dd', datetime.date(2020, 1, 1))

tickers = [tickerSymbol, '^BVSP']
dataFrame = pd.DataFrame()
for t in tickers:
    dataFrame[t] = wb.DataReader(t, data_source='yahoo', start=tickerBuyDate)['Adj Close']


st.line_chart((dataFrame/dataFrame.iloc[0]*100))
