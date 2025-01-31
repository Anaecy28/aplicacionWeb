import streamlit as st 
import pandas as pd 
from google.cloud import firestore 
from google.oauth2 import service_account
import json 

st.title('Mi primera aplicacion')

sidebar = st.sidebar

sidebar.title("Esta es la barra lateral")
sidebar.write("Aqui van los elementos de entrada")

st.title("Informacion sobre el conjunto de datos")
st.header("Descripcion de datos")
st.write("""Este es un simple ejemplo

¡¡ SE LOGROOO!!

""")
