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
    '食材': [food1, 2, 3, 4],
    '賞味期限': [10, 20, 30, 40]}))



left_column,right_column = st.columns(2)  


food1 = st.date_input('1つ目の食材の賞味期限はいつですか？',)
left_column.write(food1)   
    
@st.cache(allow_output_mutation=True)
def cache_lst1():
    lst1 = []
    return lst1
lst1 = cache_lst1()
input = st.text_input('食材は何ですか？')
if input:
    lst1.append(input)    

if st.checkbox('delete1'):
    delete = st.selectbox('食べたらリストから削除しましょう', options=lst1)
    if st.button('Delete1'):
        lst1.remove(delete)
        st.success(f'Delete1 : {delete}')
        
st.table(lst1)