import streamlit as st


abt = st.Page(
    page="views/about.py",
    title="About",
    icon=":material/home:"
)

cont = st.Page(
    page="views/contact.py",
    title="Contact",
    icon=":material/contact_mail:"
)

ser = st.Page(
    page="views/service.py",
    title="Service",
    icon=":material/build:"
)

prof = st.Page(
    page="views/profile.py",
    title="Profile",
    icon=":material/person:"
)

pg = st.navigation(pages=[abt, cont, ser, prof])

st.logo("psy.webp")

pg.run()