# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 06:53:24 2022

@author: DAZZ
"""
# importing libs
import streamlit as st
import pandas as pd
import numpy as np

# header text

st.header('Line Chart')

# create a dataframe

chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns=['a','b','c'])

# create a line chart
st.line_chart(chart_data)