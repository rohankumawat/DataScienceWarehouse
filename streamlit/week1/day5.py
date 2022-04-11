# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 09:12:45 2022

@author: DAZZ
"""

import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

# header text for the app

st.header('Elements of st.write')

# example 1
# basic use is to display text and Markdown-formatted text

st.write('Hello *World!* :sunglasses:')

# example 2
# can display other types of data too
st.write(1234)

# example 3
# dataframes can also be displayed here

df= pd.DataFrame({
    'first_col' : [1, 2, 3, 4, 5],
    'second_col' : [10, 20, 30, 40, 50]
    })

st.write(df)

# example 4
# you can pass multiple arguments too

st.write('Below is a Dataframe: ', df, 'Above is a Dataframe.')

# example 5
# you can also display plot
df2 = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c'])

c = alt.Chart(df2).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

st.write(c)