import streamlit as st 
import pandas as pd 
from google.cloud import firestore 
from google.oauth2 import service_account
import json 

try:
    config = toml.load(".streamlit/secrets.toml")
    # Acceder a la clave 'textkey'
    textkey = config.get("textkey", "Default value if not found")
    print(textkey)  # Para verificar que el valor se haya cargado correctamente
except Exception as e:
    print(f"Error al cargar el archivo TOML: {e}")
