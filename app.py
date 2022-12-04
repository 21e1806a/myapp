# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st
st.title("賞味期限リスト")
text = st.text_input('食材を追加してください')
d = st.date_input(
    "賞味期限はいつですか？",)
st.write('賞味期限は:', d)