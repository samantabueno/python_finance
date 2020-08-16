import streamlit as st
from pandas_datareader import data as wb
import datetime
import pandas as pd

st.write("""
# Calculating the Annual Simple Return 
""")

options = st.multiselect(
     'Select companies:',
     ['LREN3.SA', 'WEGE3.SA', 'MULT3.SA', 'EGIE3.SA', 'ITSA4.SA', 'MGLU3.SA', 'TRIS3.SA'],
     ['LREN3.SA'])

year = st.slider('Year:', 1990, 2020)
date_sta = datetime.date(year, 1, 1)
date_end = datetime.date(year, 12, 31)
ind = pd.DataFrame()
annual_ret = pd.DataFrame()

if st.button('Find'):
    for v in options:
        ind[v] = wb.DataReader(v, data_source='yahoo', start=date_sta, end=date_end)['Adj Close']

    sim_ret = (ind / ind.shift(1)) - 1
    annual_ret['Simple return(%)'] = sim_ret.mean() * 250 * 100
    st.write(annual_ret)

