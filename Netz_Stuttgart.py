import geopandas as gpd
from shapely.geometry import Polygon
import matplotlib.pyplot as plt
import contextily as ctx

# Gegebene Koordinatenliste
koordinaten = [
    (48.95, 8.95),
    (48.65, 8.95),
    (48.65, 9.45),
    (48.95, 9.45)
]

# Erstelle ein Polygon aus den Koordinaten
polygon = Polygon([(xy[1], xy[0]) for xy in koordinaten])

# Erstelle ein GeoDataFrame mit dem Koordinatenbezugssystem EPSG:4326
gdf = gpd.GeoDataFrame(index=[0], geometry=[polygon], crs="EPSG:4326")

# Transformiere das Koordinatensystem zu EPSG:3857 (für die Darstellung mit OSM)
#gdf = gdf.to_crs(epsg=25832)

# Speichern als Shapefile
gdf.to_file("./Layer/stuttgart.shp")

# Plotten des Polygons auf einem OSM-Hintergrund
fig, ax = plt.subplots(figsize=(10, 10))
gdf.plot(ax=ax, alpha=0.5, edgecolor='red')

# Füge den OSM-Hintergrund hinzu
#ctx.add_basemap(ax, crs=gdf.crs.to_string())

# Zeige die Karte
plt.show()
