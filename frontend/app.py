import streamlit as st

# Markdown code similar to R 
# The number of ## is the header heirarchy 
# st.markdown("# Rockets Player Finder") 
# st.markdown("""This is a streamlit application that consumes a FastAPI for Houston Rockets players.""") 
# st.markdown("""We use endpoints such as create, read, update, and delete players from our player database.""")

pages =[
    st.Page("pages/home.py", title ="Home"),
    st.Page("pages/player_finder.py", title ="PlayerFinder"),
    st.Page("pages/dashboard.py", title ="Dashboard")
]

pg = st.navigation(pages)

pg.run()
