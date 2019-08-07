import folium
import pandas

# Read data from file
data = pandas.read_csv('Volcanoes.txt')
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])

html = """
    <h4>Volcano information:</h4>
    Height: %s m
"""
# Base of map + starting point
map = folium.Map(location=[-33.892055, 150.959063], zoom_start=3)

fg = folium.FeatureGroup(name='My Map')

# Loop + add point from data location
for lt, ln, el in zip(lat, lon, elev):
    iframe = folium.IFrame(html=html % str(el), width=200, height=100)
    fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon=folium.Icon(color='green')))

map.add_child(fg)

map.save('Map1.html')