#!/usr/bin/env python
# coding: utf-8

# In[4]:


import ee
import geemap
Map = geemap.Map()
#Map


# In[5]:


#roi = ee.FeatureCollection("projects/ee-passeionamatamapas/assets/test1_csv") 
#url = "https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_cities.geojson"
roi = "https://raw.githubusercontent.com/ratitu/GOES-timelapse-wildfires-SP-2024/refs/heads/main/test3_csv.geojson"


# In[6]:


Map.add_point_layer(roi, popup=["Hostname", "Detalhes"], layer_name="test2_csv")
Map

