# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st

st.title("冷蔵庫の賞味期限")

food1 = st.text_input('食材は何ですか？')
term1 = st.date_input('賞味期限はいつですか？',)

food2 = st.text_input('食材は何ですか？')
term2 = st.date_input('賞味期限はいつですか？',)

food3 = st.text_input('食材は何ですか？')
term3 = st.date_input('賞味期限はいつですか？',)

food3 = st.text_input('食材は何ですか？')
term3 = st.date_input('賞味期限はいつですか？',)

food4 = st.text_input('食材は何ですか？')
term4 = st.date_input('賞味期限はいつですか？',)

import pandas as pd
df=pd.DataFrame({
    '食材':pd.Series([food1, food2, food3, food4], index = [ 1, 2, 3, 4 ] ),
    '賞味期限': pd.Series([term1, term2, term3, term4], index = [ 1, 2, 3, 4 ] )
    }) 

df.sort_values( by = '賞味期限', ascending = True, inplace = True )