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

#construct the pop up if we want one, this allows
#us to customize what the popup looks like
def custom_html(title="Default", disc=None, link_name='more info', link=None):
    html = ''
    html+='<h1>'+title+'</h1><br>'
    if disc:
        html+=disc
    if link:
        html+='<a '+link+' > '+link_name+'</a>'
    return html
    

folium.Marker(
    [30.2672, -97.7431], 
).add_to(m)


bar1_html = custom_html('San Jac', 'fun event', 'Here','https://posh.vip/e/gen-ws-ladys-poker-night')


folium.Marker(
    [30.2706, -97.7287], 
    popup=bar1_html, 
    tooltip="Bar",
    lazy=True
).add_to(m)




def get_pos():
    try:
        return [displayedMap['last_clicked']['lat'],displayedMap['last_clicked']['lng']]
    except:
        return None


m.add_child(folium.LatLngPopup())

displayedMap = st_folium(m)

left, right = st.columns(2)
with left:
    st.write("## Tooltip")
    st.write(displayedMap["last_object_clicked_tooltip"])
with right:
    st.write("## Popup")
    st.write(displayedMap["last_object_clicked_popup"])




if get_pos():
    st.write(get_pos())




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


    