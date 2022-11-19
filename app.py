import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import streamlit as st
from configu import *

st.title('About my Project')
st.sidebar.header(Project_Name)
st.sidebar.write(Done_By)
choice=st.sidebar.radio('select Options', Menu_Options)
st.write('👋','helloharendra')