import geemap
import ee
import ipyleaflet
import os

def app():
    st.title("Wildfire Monitoring & Earth Engine API")

    st.markdown(
        """
    This data platform provides access to live updatessatellite imagery, earth engine collections and dataBC geodatasets used in wildfire monitoring and natural resource assessments.

    """
    )

    Map = geemap.Map(center=(52.5, -119), zoom=4)
    dataset_inz = ee.ImageCollection('FIRMS')
    image2 = dataset_inz.first()
    Map.addLayer(image2, {}, 'Active Fires')
    Map
