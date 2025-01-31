import streamlit as st 
import pandas as pd 
from google.cloud import firestore 
from google.oauth2 import service_account
import json 

db = firestore.Client.from_service_account_json("firebase.json")
dbNames = db.collection("names")

st.header ("Nuevo registro")

index = st.text_input ("Index")
name = st.text_input ("Name")
sex = st.selectbox('Seleccionar : ', ('F', 'M', 'Other'))

submit = st.button("Crear nuevo registro")

if index and name and sex and submit:
  doc_ref = db.collection("names").document(name) 
  doc_ref.set({
      "index": index,
      "name":  name,
      "sex": sex
  })
  st.write ("Resgitro insertado correctamente")

  names_ref = list(db.collection(u'names').stream())
  names_dict = list(map(lambda x: x.to_dict(), names_ref))
  names_dataframe =pd.DataFrame(names_dict)
  st.dataframe(names_dataframe)
