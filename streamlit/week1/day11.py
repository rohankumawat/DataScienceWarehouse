# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 07:05:45 2022

@author: DAZZ
"""

import streamlit as st

st.header('st.multiselect')

options = st.multiselect(
    'What are your favorite colors?',
    ["Green", "Yellow", "Red", "Blue"],
    ['Yellow', "Red"])

st.write("You selected: ", options)