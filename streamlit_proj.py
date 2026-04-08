import pandas as pd
import numpy as np
import streamlit as st

st.title("This is a random project")
st.html("<center><h1>HELLO</h1></center>")
pcode = """
    def fun1(): 
        print("Hello")"""
st.code(pcode,language='python')

data = pd.DataFrame(np.random.randn(20,3), columns=["A","B","C"])

st.line_chart(data)



st.logo("/Users/kshiraj/Desktop/Interface/nom.png")
btn = st.button("want good times", type="primary")
if btn:
    st.image("/Users/kshiraj/Desktop/Interface/psy.webp")