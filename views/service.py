import streamlit as st

st.title("Service")
st.write('<p style="font-size:25px;">"Not Needed"</p>', unsafe_allow_html=True)

picture = st.camera_input("Take a pic")

if picture:
    st.image(picture)