from osmnx import geocode_to_gdf
import os

gdf_paraiba = geocode_to_gdf('Paraiba, Brazil')

os.makedirs('data', exist_ok=True )

gdf_paraiba.to_file('data/paraiba.shp')
 