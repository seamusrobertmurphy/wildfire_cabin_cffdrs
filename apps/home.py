import streamlit as st
import leafmap.foliumap as leafmap
import ee


def app():

    st.title("Active Fires")

    m = leafmap.Map(locate_control=TRUE)
    m.add_basemap("SATELLITE")
    dataset_inz = ee.ImageCollection('FIRMS')
    image2 = dataset_inz.first()
    m.addLayer(image2, {}, 'Active Fires FIRMS')
    m.to_streamlit(height=700)

