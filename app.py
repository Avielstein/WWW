#!pip install google-cloud-firestore
#!pip install streamlit
#!pip install folium
#!pip install streamlit_folium


#https://blog.streamlit.io/streamlit-firestore/
#https://blog.streamlit.io/streamlit-firestore-continued/


##########################################################################
import streamlit as st
import pandas as pd
import numpy as np
from firebase import firebase
import folium
from streamlit_folium import st_folium
st.set_page_config(layout="wide")




##########################################################################
st.title('Where What When 🌎 - Austin')
firebase = firebase.FirebaseApplication('https://web-data-b7bda-default-rtdb.firebaseio.com/', None)
result = firebase.get('/',None)
#st.text(result)

st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")



##########################################################################
#MAP
##########################################################################



##########################################################################
#OPTIONS CONTAINS OUTPUT OF THE SELECTION
options = st.multiselect(
    'Show me:',
    ['Bars', 'Restruants','Events', 'Live Music', 'DJ'],
    ['Bars', 'Events'],
    placeholder="Choose an option")

##########################################################################
#LOCATIION
#austin
m = folium.Map(location=[30.2672, -97.7431], zoom_start=13)

##########################################################################
#LOCATIION
html = """
    <h1>MOSA BAR</h1><br>
    Find more info 
    <a href=https://posh.vip/e/gen-ws-ladys-poker-night>Here</a>
    """
folium.Marker(
    [30.2672, -97.7431], 
    popup=html, 
    tooltip="Bar",
    lazy=True
).add_to(m)

# call to render Folium map in Streamlit
st_data = st_folium(m, width=725)




##########################################################################
#SEARCH
##########################################################################
#https://blog.streamlit.io/create-a-search-engine-with-streamlit-and-google-sheets/
#https://docs.streamlit.io/library/api-reference/layout/st.columns

# Use a text_input to get the keywords to filter the dataframe
text_search = st.text_input("Search videos by title or speaker", value="")


col1, col2, col3 = st.columns(3)

with col1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg")
   st.caption("st.caption(")
   st.markdown("st.caption(")

with col2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg")

##########################################################################
#FOOTER
##########################################################################
#one way to center it
col1, col2, col3 = st.columns(3)
with col2:

    image = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRlcRZh6zlFELDpcxdbJ0V5K29oaiCjfrh6yg&usqp=CAU"
    link = "https://apps.apple.com/us/app/mosa-drinks-friends-rewards/id1615330534"
    #Footer
    st.markdown("[![]("+image+")]("+link+")")

##########################################################################






##########################################################################
#Keeping things clean
##########################################################################
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

hide_menu_style = """
                <style>
                #MainMenu {visibility: hidden;}
                </style>
                """
st.markdown(hide_menu_style, unsafe_allow_html=True)


    