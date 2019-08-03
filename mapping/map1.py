import folium
map = folium.Map(location=[-33.868233, 151.208067])

fg = folium.FeatureGroup(name='My Map')

for coordinates in [[-33.8, 151.3],[-34, 150]]:
    fg.add_child(folium.Marker(location=coordinates, popup='Hi i am marker', icon=folium.Icon(color='green')))

map.add_child(fg)

map.save('Map1.html')