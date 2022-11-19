import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import streamlit as st
from configu import *

st.title('About my Project')
st.sidebar.header(Project_Name)
st.sidebar.write(Done_By)
choice=st.sidebar.radio('select Options', Menu_Options)


if choice =='Home' :
    st.image('image/SoftwareInstall.jpeg')
if choice=='About':
    st.image('image/Webcamset.jpeg')
if choice=='Contact':
    st.image('image/maskgirls.png')    
if choice=='Services':
    st.image('image/WhatsApp Image 2021-05-25 at 5.46.51 PM.jpeg')    

st.write('👋','helloharendra')