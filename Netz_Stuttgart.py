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

koordinaten_Fasanenhof = [
    (5395423.55,512551.47),
    (5395747.69,512392.99),
    (5395828.59,512111.31),
    (5395792.20,512051.11),
    (5395720.82,512049.43),
    (5395457.70,512091.99),
    (5395324.18,512129.09),
    (5395212.22,512196.29),
    (5394970.09,512339.79),
    (5394893.11,512505.69),
    (5394907.37,512560.51),#UW
    (5394589.67,512682.31),
    (5394546.28,512557.71),
    (5394421.72,512578.71),
    (5394456.71,512753.71),
    (5394827.59,512711.71),
    (5394912.97,512598.31),#UW
    (5394924.60,512648.49),
    (5395226.91,512679.29),
    (5395243.01,512607.19),
    (5395226.91,512512.69),
    (5395322.36,512464.11),
    (5395412.63,512478.11)
]

# Erstelle ein Polygon aus den Koordinaten
polygon = Polygon([(xy[1], xy[0]) for xy in koordinaten_Fasanenhof])

# Erstelle ein GeoDataFrame mit dem Koordinatenbezugssystem EPSG:4326
gdf = gpd.GeoDataFrame(index=[0], geometry=[polygon], crs="EPSG:25832")

# Transformiere das Koordinatensystem zu EPSG:3857 (für die Darstellung mit OSM)
#gdf = gdf.to_crs(epsg=25832)

# Speichern als Shapefile
gdf.to_file("./Layer/Fasanenhof.shp")

# Plotten des Polygons auf einem OSM-Hintergrund
fig, ax = plt.subplots(figsize=(10, 10))
gdf.plot(ax=ax, alpha=0.5, edgecolor='red')

# Füge den OSM-Hintergrund hinzu
#ctx.add_basemap(ax, crs=gdf.crs.to_string())

# Zeige die Karte
plt.show()
