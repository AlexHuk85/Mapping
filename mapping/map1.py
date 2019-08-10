import folium
import pandas

# Read data from file
data = pandas.read_csv('Volcanoes.txt')
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])
name = list(data['NAME'])

# Function - Change icon color by elevation
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
map = folium.Map(location=[-33.892055, 150.959063], zoom_start=3, tiles='cartodbpositron')


fgv = folium.FeatureGroup(name='Volcanoes in USA')

# Loop + add point from data location
for lt, ln, el in zip(lat, lon, elev):
    #iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=6, fill=True,
    popup=str(el) + ' m', fill_color=Icon_Color(el), color='grey', fill_opacity=0.7)) 
    #popup=folium.Popup(iframe), icon=folium.Icon(color=Icon_Color(el))))

fgp = folium.FeatureGroup(name='Population')

fgp.add_child(folium.GeoJson(data=(open('world.json', 'r', encoding='utf-8-sig').read()),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))


map.add_child(fgv)
map.add_child(fgp)

# Add layer control
map.add_child(folium.LayerControl())

map.save('Map1.html')