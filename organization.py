import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.title("Clinical Staff Registration Page")

img = Image.open('apple.png')

st.image(img)


st.text_input("Name")

st.selectbox("Gender", ['Male','Female','Others'])

st.number_input("Staff Number", step=1)

st.sidebar.selectbox('Location',['Headquarter', 'Benue', 'Ogun', 'Ondo', 'Oyo', 'Plateau'])

st.sidebar.selectbox('Current Position',['Director', 'Associate Director', 'Senior Technical Advisor', 'Advisor', 'Senior Technical Officer', \
                                 'Technical Officer', 'Assistant Technical Officer', 'Senior Technical Associate', 'Technical Associate'])
st.text_input("Duration in Employment")

st.date_input('Date of First Employment')

st.sidebar.selectbox('Entry Position', ['Director', 'Associate Director', 'Senior Technical Advisor', 'Advisor', 'Senior Technical Officer', \
                                 'Technical Officer', 'Assistant Technical Officer', 'Senior Technical Associate', 'Technical Associate'])

st.sidebar.selectbox('Your Preferred Thematic Area', ['Adult ART', 'Paediatric ART', 'Continuity of Treatment', 'TB/HIV', 'Non Communicable Diseases', \
                                 'Third 95', 'Continuous Quality Improvement', 'Infection Prevention & Control'])


if st.checkbox('I confirm that information provided are true'):
    st.balloons()
else:
    st.warning('Click the checkbox to confirm')

if st.button('Submit'):
    st.write('Thank you for submitting')
    




 