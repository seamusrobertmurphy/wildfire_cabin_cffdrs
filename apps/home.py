import streamlit as st
import leafmap.foliumap as leafmap


def app():
    st.title("Wildfire & Earth Engine API")

    st.markdown(
        """
    This platform provides access to NASA satellite imagery, earth engine collections and dataBC geodatasets used in wildfire monitoring and natural resource assessments.

    """
    )

    m = leafmap.Map(locate_control=True)
    m.add_basemap("SATELLITE")
    m.to_streamlit(height=700)

