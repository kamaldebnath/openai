import openai
import os
import streamlit as st
import urllib.request as rq
# import config

# openai.api_key=config.api
openai.api_key=st.secrets['api']
st.title("Image Generator Using AI")
promt=st.text_input("Give a detailed description")

if promt:
  response = openai.Image.create(
    prompt=promt,
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  st.image(image=image_url)
