import streamlit as st
import pandas as pd 
import httpx    
import requests



data = requests.get("http://127.0.0.1:8000/players/").json()

df = pd.DataFrame(data)

st.markdown("# Player Dashboard")

st.markdown("#### Some statistics and metrics about our players")

st.markdown("## KPIs")

cols = st.columns(3)
# This is the columns that show the KPIs 
# We query the information with certain paramaters
with cols[0]:
    st.metric("total players", len(df))
with cols[1]:
    st.metric("older players", len(df.query("player_age > 35")))
with cols[2]:
    st.metric("newer players", len(df.query("player_age < 25")))


st.markdown("## Age distrbution")
ax = df["player_age"].plot(
    kind = "hist", xlabel = "age", title = "distribution of age of all players"
)

fig = ax.get_figure()

st.pyplot(fig)



st.markdown("## All available players")
st.dataframe(df)