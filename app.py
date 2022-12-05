# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st

st.title("冷蔵庫の賞味期限")

left_column,right_column = st.columns(2)

food1 = st.date_input('1つ目の食材の賞味期限はいつですか？',)
left_column.write(food1)
import pandas as pd
st.table(pd.DataFrame({
    '食材': [1, 2, 3, 4],
    '賞味期限': [food1, 20, 30, 40]}))