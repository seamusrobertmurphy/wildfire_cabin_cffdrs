import streamlit as st
import leafmap.foliumap as leafmap
import geemap
import ee
import ipyleaflet
import os

def app():
    st.title("Wildfire Monitoring & Earth Engine API")

    st.markdown(
        """
    This data platform provides access to NASA satellite imagery, earth engine collections and dataBC geodatasets used in wildfire monitoring and natural resource assessments.

    """
    )

    m = geemap.Map(center=(52.5, -119), zoom=4)
    dataset_inz = ee.ImageCollection('FIRMS')
    image2 = dataset_inz.first()
    m.addLayer(image2, {}, 'Active Fires')

