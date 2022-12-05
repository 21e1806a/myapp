# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st
text = st.text_input('食材を追加してください')
d = st.date_input(
    "賞味期限はいつですか？",)

st.title("冷蔵庫の賞味期限")

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
    
food1 = st.date_input('1つ目の食材の賞味期限はいつですか？',)
left_column.write(food1)    

if st.checkbox('delete1'):
    delete = st.selectbox('食べたらリストから削除しましょう', options=lst1)
    if st.button('Delete1'):
        lst1.remove(delete)
        st.success(f'Delete1 : {delete}')
        
st.table(lst1)







st.title("やることリスト")
    
import datetime
from dateutil.relativedelta import relativedelta
from datetime import date

left_column,right_column = st.columns(2)  


def main():
    homework1 = st.date_input('課題1の提出期限を書いてください。',
                             min_value=date.today(),
                             value=date.today(),
                             )
    left_column.write(homework1)   
    
    

    kyou1 = datetime.date.today()            
    if homework1 <= kyou1 + relativedelta(days=+1):
        right_column.write('急いで課題1に取り組みましょう!!!')
    elif homework1 <= kyou1 + relativedelta(weeks=+1):
        right_column.write('そろそろ課題1に取り組みましょう!!')
    else :
        right_column.write('計画的に課題1を勧めましょう！')
           
if __name__ == '__main__':
    main() 
    
@st.cache(allow_output_mutation=True)
def cache_lst1():
    lst1 = []
    return lst1

lst1 = cache_lst1()
input = st.text_input('課題1の内容')

if input:
    lst1.append(input)
if st.checkbox('delete1'):
    delete = st.selectbox('課題1の削除する要素を選択して下さい', options=lst1)
    if st.button('Delete1'):
        lst1.remove(delete)
        st.success(f'Delete1 : {delete}')

if st.checkbox('change1'):
    change_from = st.selectbox('課題1の変更する要素を選択して下さい', options=lst1)
    change_index = lst1.index(change_from)
    change_to = st.text_input('どのように課題1を変更しますか')
    if st.button('Change1'):
        lst1.remove(change_from)
        lst1.insert(change_index, change_to)
        st.success(f'Change1 {change_from} to {change_to}')
        
st.table(lst1)



progress1 = st.slider('課題1の進捗は？',0, 100, 50)
'課題1進捗：',progress1