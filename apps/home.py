import streamlit as st
import leafmap.foliumap as leafmap
import geemap.foliumap as geemap


def app():
    st.title("Home")

    st.markdown(
        """
    We acknowledge the use of imagery provided by services from NASA's Global Imagery Browse Services (GIBS), part of NASA's Earth Observing System Data and Information System (EOSDIS).
    """
    )

    m = geemap.Map(locate_control=True)
    m.add_basemap("TERRAIN")
    dem = ee.Image("USGS/SRTMGL1_003")
    vis_params = {
    "min": 0,
    "max": 4000,
    "palette": ["006633", "E5FFCC", "662A00", "D8D8D8", "F5F5F5"],
}
    m.addLayer(dem, vis_params, "SRTM DEM", True, 0.5)
    m.to_streamlit(height=700)
