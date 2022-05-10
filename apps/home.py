import streamlit as st
import leafmap.foliumap as leafmap
import geemap
import ee
import ipyleaflet
import os



def app():
    st.title("Active Fires")

    st.markdown(
        """
    We acknowledge the use of data and/or imagery from NASA's Fire 
    Information for Resource Management System (FIRMS) 
    (https://earthdata.nasa.gov/firms), part of NASA's 
    Earth Observing System Data and Information System (EOSDIS).

    FIRMS distributes near real-time and standard fire products from: 
    Moderate Resolution Imaging Spectroradiometer (MODIS) 
    from the Terra and Aqua platforms, and Visible Infrared Imaging 
    Radiometer Suite (VIIRS) (375m) from the Suomi NPP and 
    NOAA-20 platforms.  
    
    """
    )


    m = leafmap.Map(locate_control=TRUE)
    m.add_basemap("SATELLITE")
    m.to_streamlit(height=700)
    dataset_inz = ee.ImageCollection('FIRMS')
    image2 = dataset_inz.first()
    m.addLayer(image2, {}, 'Active Fires')
    m
