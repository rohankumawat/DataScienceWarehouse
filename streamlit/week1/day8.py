# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 10:08:39 2022

@author: DAZZ
"""

import streamlit as st
from datetime import time, datetime

st.header('st.slider')

# example 1

st.subheader('Slider')

# minimum, maximum, default value respectively

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

# example 2

st.subheader('Range Slider')

# allows selection of a lower and upper bound value pair

values = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0))
st.write('Values: ', values)

# example 3

st.subheader('Range time slider')

# allows selection of a lower and upper bound value pair of datetime

appointment = st.slider(
    'Schedule your appointment: ',
    value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for: ", appointment)

# example 4

st.subheader('Datetime slider')

start_time = st.slider(
    "When do you start?",
    value=datetime(2020, 1, 1, 9, 30),
    format="MM/DD/YY - hh:mm")
st.write("Start time: ", start_time)