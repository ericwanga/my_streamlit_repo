
import streamlit as st
import pandas as pd

st.title('My Title')
st.title('Another :blue[Blue Title] :sunglasses:')
st.header('My Header')
st.text('🥑🍞 Some text')
st.text('🥣 texts')
st.text('🥗 text')
st.text('🐔 text')
st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
st.dataframe(my_fruit_list)
