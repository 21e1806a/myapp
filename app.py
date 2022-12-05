# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st

st.title("冷蔵庫の賞味期限")

food1 = st.text_input('食材は何ですか？')
term1 = st.date_input('の食材の賞味期限はいつですか？',)

food2 = st.text_input('食材は何ですか？')
term2 = st.date_input('の賞味期限はいつですか？',)

food3 = st.text_input('食材は何ですか？')
term3 = st.date_input('の賞味期限はいつですか？',)

food3 = st.text_input('食材は何ですか？')
term3 = st.date_input('の賞味期限はいつですか？',)

food4 = st.text_input('食材は何ですか？')
term4 = st.date_input('の賞味期限はいつですか？',)

import pandas as pd
st.table(pd.DataFrame({
    '食材':[food1, food2, food3, food4],
    '賞味期限': [term1, term2, term3, term4
             ]}))