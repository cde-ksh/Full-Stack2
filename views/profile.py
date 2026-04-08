import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.markdown('<h1 style="text-align: center; font-size: 50px;">Profile</h1>', unsafe_allow_html=True)

col1, space, col2 = st.columns([4,6,4])

with col1:
    st.header("Profile image: ")
    st.image("https://archives.bulbagarden.net/media/upload/thumb/3/3f/0054Psyduck.png/500px-0054Psyduck.png")

with col2:
    st.header("Contact info:")
    st.write('<p style="font-size:25px;">Name: PsyDuck</p>', unsafe_allow_html=True)
    st.write('<p style="font-size:25px;">Email: GCEA@aaaa.com</p>', unsafe_allow_html=True)
    st.write('<p style="font-size:25px;">Phone: Nokia</p>', unsafe_allow_html=True)

st.header("Career: None")

st.divider()

df = pd.DataFrame({
    'Name': ['PsyDuck', 'Pikachu', 'Charizard'],
    'Email': ['GCEA@aaaa.com', 'pika@aaaa.com', 'charizard@aaaa.com'],
    'Call' : ['PsyyyyyDuck', 'Pika-Pika', 'Rawrrrr'],
    'Speciality': ['Headache', 'Thunder-bolt', 'Fire-blast'],
    'Type': ['Water', 'Electric', 'Fire']
})

df.index = df.index + 1

st.table(df)
