import streamlit as st
from Multiapp import Multipage
from apps import Home,Details


def apps():
    app = Multipage()
    app.add_page("Home", Home.app)
    app.add_page("Details",Details.app)
    app.run()
apps()
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")



