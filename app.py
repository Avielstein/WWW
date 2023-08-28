import streamlit as st

st.header('Test4 🌎!')

from firebase import firebase
firebase = firebase.FirebaseApplication('https://web-data-b7bda-default-rtdb.firebaseio.com/', None)
result = firebase.get('/',None)
st.text(result)


import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randn(10, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(df)


import folium
from streamlit_folium import st_folium

# center on Liberty Bell, add marker
m = folium.Map(location=[39.949610, -75.150282], zoom_start=16)
folium.Marker(
    [39.949610, -75.150282], popup="Liberty Bell \n\n Testing longer script", tooltip="Liberty Bell"
).add_to(m)

# call to render Folium map in Streamlit
st_data = st_folium(m, width=725)


    