import streamlit as st
import pandas as pd
import requests
# streamlit run app.py to run streamlit
# Make sure we are in the correct file (Rocket_API)
# uv add requests into terminal

# This allows to grab players data
# import requests 


# Grabbing all players data 
# .json gives all json data 
all_players = requests.get("http://127.0.0.1:8000/players/").json()

df = pd.DataFrame(all_players)

# Loop over all players and get their names
all_player_names = [player.get("player_name") for player in all_players]
# st.write(all_player_names) #shows all players names 

# This is the header 
st.markdown ("# PlayerFinder")
# This shows all players and their data

# This is the dropdown menu that shows all the players in the database
# The selected player_name by the user will then call the API that gets player name
selected_name = st.selectbox("Choose your Player", options = all_player_names)

# Get request to FastAPI and get data, then write it out 
selected_player = requests.get(f"http://127.0.0.1:8000/players/{selected_name}").json()

st.markdown(f"**Player Name:** {selected_player['player_name']}")
st.markdown(f"**Height in Inches:** {selected_player['height_inches']}")
st.markdown(f"**Player Age:** {selected_player['player_age']}")

if st.button("list players under 35 years old"):
    filtered_df = df.query("player_age < 35")

    st.dataframe(filtered_df)

    for column in filtered_df.columns:
        st.metric(
            label = column,
            value = filtered_df[column].iloc[0]
        )
else:
    st.write("Click the button")

st.button("Search")





                            










