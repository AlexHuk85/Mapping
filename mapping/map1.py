import folium
import pandas

# Read data from file
data = pandas.read_csv('Volcanoes.txt')
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])
name = list(data['NAME'])

# Function - Change icon color
def Icon_Color(el):
    if el < 1000:
        return 'green'
    elif el < 3000:
        return 'orange'
    else:
        return 'red'

html = """
    Volcano name:<br>
    <a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a>
    <br>
    Height: %s m
"""

# Base of map + starting point
map = folium.Map(location=[-33.892055, 150.959063], zoom_start=3)

fg = folium.FeatureGroup(name='My Map')

# Loop + add point from data location
for lt, ln, el, name in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
    fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon=folium.Icon(color=Icon_Color(el))))

map.add_child(fg)

map.save('Map1.html')