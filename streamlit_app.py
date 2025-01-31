import streamlit as st 
import pandas as pd 
from google.cloud import firestore 
from google.oauth2 import service_account
import json 

st.write(st.secrets)
