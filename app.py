# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st

st.title("冷蔵庫の賞味期限")

left_column,right_column = st.columns(2)

food1 = st.ｔext_input('1つ目の食材は何ですか？',)
left_column.write(food1)

term1 = st.date_input('1つ目の食材の賞味期限はいつですか？',)
left_column.write(term1)

food2 = st.text_input('2つ目の食材は何ですか？',)
left_column.write(food2)

term2 = st.date_input('2つ目の食材の賞味期限はいつですか？',)
left_column.write(term2)

food3 = st.text_input('3つ目の食材は何ですか？',)
left_column.write(food3)

term3 = st.date_input('3つ目の食材の賞味期限はいつですか？',)
left_column.write(term3)

food4 = st.text_input('4つ目の食材は何ですか？',)
left_column.write(food4)

term4 = st.date_input('4つ目の食材の賞味期限はいつですか？',)
left_column.write(term4)

food5 = st.text_input('5つ目の食材は何ですか？',)
left_column.write(food5)

term5 = st.date_input('5つ目の食材の賞味期限はいつですか？',)
left_column.write(term5)

food6 = st.text_input('6つ目の食材は何ですか？',)
left_column.write(food6)

term6 = st.date_input('6つ目の食材の賞味期限はいつですか？',)
left_column.write(term6)

food7 = st.text_input('7つ目の食材は何ですか？',)
left_column.write(food7)

term7 = st.date_input('7つ目の食材の賞味期限はいつですか？',)
left_column.write(term7)

food8 = st.text_input('8つ目の食材は何ですか？',)
left_column.write(food8)

term8 = st.date_input('8つ目の食材の賞味期限はいつですか？',)
left_column.write(term8)

food9 = st.text_input('9つ目の食材は何ですか？',)
left_column.write(food9)

term9 = st.date_input('9つ目の食材の賞味期限はいつですか？',)
left_column.write(term9)

food10 = st.text_input('10個目の食材は何ですか？',)
left_column.write(food10)

term10 = st.date_input('10個目の食材の賞味期限はいつですか？',)
left_column.write(term10)


import pandas as pd
st.table(pd.DataFrame({
    '食材': [food1, food2, food3, food4, food5, food6, food7, food8, food9, food10],
    '賞味期限': [term1, term2, term3, term4, term5, term6, term7, term8, term9, term10]}))