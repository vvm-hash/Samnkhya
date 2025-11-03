import requests
import pandas as pd
import plotly.express as px
import geopandas as gpd

# ----------------------------------------
# CONFIGURATION
# ----------------------------------------
SENTIMENT_API = "http://13.204.162.142:8000/api/sentiments"
GEOJSON_URL = "https://raw.githubusercontent.com/adarshbiradar/maps-geojson/master/india.json"
# ----------------------------------------

# --- STEP 1: Fetch sentiment data ---
print("Fetching sentiment data...")
response = requests.get(SENTIMENT_API)
response.raise_for_status()
data = response.json()

print("Sample data:", data[:3] if isinstance(data, list) else list(data.items())[:3])

# Handle both possible formats
if isinstance(data, dict):
    df = pd.DataFrame(list(data.items()), columns=["State", "Sentiment"])
else:
    df = pd.DataFrame(data)

# Clean up
df.columns = [c.strip().title() for c in df.columns]
df["State"] = df["State"].str.title()

# --- STEP 2: Load India GeoJSON ---
print("Loading India GeoJSON...")
gdf = gpd.read_file(GEOJSON_URL)
print("Columns in GeoJSON:", list(gdf.columns))

# Use the correct key for state names
gdf["State"] = gdf["st_nm"].str.title()

# --- STEP 3: Merge sentiment data with map ---
merged = gdf.merge(df, on="State", how="left")

# --- STEP 4: Create Plotly Heatmap ---
fig = px.choropleth(
    merged,
    geojson=merged.__geo_interface__,
    locations=merged.index,
    color="Sentiment",
    hover_name="State",
    color_continuous_scale="RdYlGn",  # Red-negative → Green-positive
    title="Sentiment Heatmap of India",
)

fig.update_geos(fitbounds="locations", visible=False)
fig.update_layout(
    title_x=0.5,
    margin={"r": 0, "t": 40, "l": 0, "b": 0}
)

# --- STEP 5: Export HTML ---
fig.write_html("india_sentiment_heatmap.html")
print("✅ Map created successfully! Open 'india_sentiment_heatmap.html' in your browser.")
