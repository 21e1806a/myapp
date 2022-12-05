# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st

st.title("冷蔵庫の賞味期限")

food1 = st.text_input('一つ目の食材は何ですか？')
term1 = st.date_input('一つ目の賞味期限はいつですか？',)

food2 = st.text_input('二つ目の食材は何ですか？')
term2 = st.date_input('二つ目の賞味期限はいつですか？',)

food3 = st.text_input('三つ目の食材は何ですか？')
term3 = st.date_input('三つ目の賞味期限はいつですか？',)

import pandas as pd
df=pd.DataFrame({'賞味期限': pd.Series([term1, term2, term3], index = [food1, food2, food3])
    }) 

df.sort_values( by = '賞味期限', ascending = True, inplace = True )