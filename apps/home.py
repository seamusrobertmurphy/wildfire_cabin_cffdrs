import streamlit as st
import leafmap.foliumap as leafmap


def app():
    st.title("Home")

    st.markdown(
        """
    We acknowledge the use of imagery provided by services from NASA's Global Imagery Browse Services (GIBS), part of NASA's Earth Observing System Data and Information System (EOSDIS).
    """
    )

    m = leafmap.Map(locate_control=True)
    m.add_basemap("ROADMAP")
    m.to_streamlit(height=700)
