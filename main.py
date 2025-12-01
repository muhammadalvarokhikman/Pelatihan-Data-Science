import streamlit as st
import pandas as pd
import numpy as np 

st.write("Pelatihan Data Science Kolaborasi S1-Statistika dan S1-Sains Data")
all_users = ["Muhammad", "Alvaro", "Khikman"]
with st.container(border=True):
    users = st.multiselect("Pilih nama user", all_users)
    
np.random.seed(42)
data = pd.DataFrame(np.random.randn(10, len(users)), columns=users)

tab1, tab2 = st.tabs(["Chart", "Dataframe"])
tab1.line_chart(data, height=250)
tab2.dataframe(data, height=250, width="stretch")