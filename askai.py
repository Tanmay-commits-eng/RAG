import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import requests
question = st.text_input("Ask Me Anything")

if st.button("Ask AI"):

    response = requests.post("http://localhost:11434/api/generate",
        json={
            "model": "mistral",
            "prompt": question,
            "stream": False,
            "temperature": 0.7
            #"messages":[{"role": "user", "content": question}]
        }
    )
    print("Status:", response.status_code)
    print("Content-Type:", response.headers.get("Content-Type"))
    print("Response:", response.text)

    answer = response.json()["response"]

    st.write(answer)