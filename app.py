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
    '食材':[1, 2, 3, 4],
    '賞味期限': [food1, food2, food3, food4]}))



left_column,right_column = st.columns(2)  


food1 = st.date_input('1つ目の食材の賞味期限はいつですか？',)
left_column.write(food1)   
    
@st.cache(allow_output_mutation=True)
def cache_DateFrame():
    pd.DateFrame = []
    return pd.DateFrame
DateFrame = cache_DateFrame()
input = st.text_input('食材は何ですか？')
if input:
    pd.DateFrame.append(input)    

if st.checkbox('delete1'):
    delete = st.selectbox('食べたらリストから削除しましょう', options=pd.DateFrame)
    if st.button('Delete1'):
        pd.DateFrame.remove(delete)
        st.success(f'Delete1 : {delete}')
        
st.table(pd.DateFrame)