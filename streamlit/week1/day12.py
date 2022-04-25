# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 08:52:33 2022

@author: DAZZ
"""

import streamlit as st

st.header('st.checkbox')

st.write('What would you loke to order?')

icecream = st.checkbox('Ice Cream')
coffee = st.checkbox('Coffee')
cola = st.checkbox('Cola')

if icecream:
    st.write("Great! Here's some :icecream:")
    
if coffee:
    st.write("Volllaa! Here's your coffee :coffee:")

if cola:
    st.write("There you go! :cup_with_straw:")