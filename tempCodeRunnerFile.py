import streamlit as st

st.title("Streamlit Page ")

st.divider()
st.header("This is a header")
st.divider()
st.write("This is a write method")
st.image("/Users/kshiraj/Desktop/Interface/l.webp")
st.logo("/Users/kshiraj/Desktop/Interface/l.webp")
btn = st.button("click", type='primary')
if btn:
    st.markdown("**HELLO** ")
st.markdown('*helllo*')
st.markdown('**helllo**')
st.markdown('**BIHARI**')