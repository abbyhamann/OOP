import streamlit as st
from PIL import Image

col1, col2 = st.columns((4, 5))

with col1:
    st.title("My Resume")
    st.header("Justus Selwyn")
with col2:
    image = Image.open('Abby.PNG')
    st.image(image, width=200)

st.markdown("**About Me**")
st.text("I am an Academician, Researcher, and a Musician.")
st.text("I teach computer science at JBU.")

st.markdown("**Education**")
st.text("High School Graduate")
st.text("Current student at JBU")
st.markdown("**Work Experience**")
st.text("2 years of nannying")
st.text("6 months as Law Firm Receptionist")

st.divider()
st.markdown("**Contact me:**")
st.text_input("Your Name:")
st.text_input("Your Email:")
message = st.text_area("Your message")
st.button("Send Message")