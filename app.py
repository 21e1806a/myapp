# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st

st.title("冷蔵庫の賞味期限")

left_column,right_column = st.columns(2)
food1 = st.text_input('食材は何ですか？')
term1 = st.date_input(food1,'の食材の賞味期限はいつですか？',)
left_column.write(term1)

food2 = st.text_input('食材は何ですか？')
term2 = st.date_input(food2,'の賞味期限はいつですか？',)
left_column.write(term2)

food3 = st.text_input('食材は何ですか？')
term3 = st.date_input(food3,'の賞味期限はいつですか？',)
left_column.write(term3)

food3 = st.text_input('食材は何ですか？')
term3 = st.date_input(food3,'の賞味期限はいつですか？',)
left_column.write(term3)

food4 = st.text_input('食材は何ですか？')
term4 = st.date_input(food4,'の賞味期限はいつですか？',)
left_column.write(term4)

import pandas as pd
st.table(pd.DataFrame({
    '食材':[food1, food2, food3, food4],
    '賞味期限': [term1, term2, term3, term4
             ]}))