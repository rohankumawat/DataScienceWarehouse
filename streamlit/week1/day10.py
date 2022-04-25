# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 06:59:12 2022

@author: DAZZ
"""

#import libs

import streamlit as st

#header

st.header('st.selectbox')

# selectbox

option = st.selectbox(
    'What is you favourite color?',
    ('Blue', 'Red', 'Green'))

st.write('Your favourite color is ', option)