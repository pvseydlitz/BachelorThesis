import geopandas as gpd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn')

#%matplotlib inline

plz_shape_df = gpd.read_file('Data/PLZ-Gebiete/plz-gebiete.shp', dtype={'plz': str})

#print(plz_shape_df.head())

#Simple map of Germany
plt.rcParams['figure.figsize'] = [16, 11]

top_cities = {
    'Berlin': (13.404954, 52.520008),
    'Cologne': (6.953101, 50.935173),
    'Düsseldorf': (6.782048, 51.227144),
    'Frankfurt am Main': (8.682127, 50.110924),
    'Hamburg': (9.993682, 53.551086),
    'Leipzig': (12.387772, 51.343479),
    'Munich': (11.576124, 48.137154),
    'Dortmund': (7.468554, 51.513400),
    'Stuttgart': (9.181332, 48.777128),
    'Nürnberg': (11.077438, 49.449820),
    'Hannover': (9.73322, 52.37052)
}

fig, ax = plt.subplots()

plz_shape_df.plot(ax=ax, color='orange', alpha=0.8)

# Plot cities.
for c in top_cities.keys():
    # Plot city name.
    ax.text(
        x=top_cities[c][0],
        # Add small shift to avoid overlap with point.
        y=top_cities[c][1] + 0.08,
        s=c,
        fontsize=12,
        ha='center',
    )
    # Plot city location centroid.
    ax.plot(
        top_cities[c][0],
        top_cities[c][1],
        marker='o',
        c='black',
        alpha=0.5
    )

ax.set(
    title='Germany',
    aspect=1.3,
    facecolor='lightblue'
)
plt.show()

#Merge plz and ort
plz_region_df = pd.read_csv('./Data/zuordnung_plz_ort.csv', sep=',', dtype={'plz': str})
plz_region_df.drop('osm_id', axis=1, inplace=True)

germany_df = pd.merge(left=plz_shape_df, right=plz_region_df, on='plz',how='inner')
germany_df.drop(['note'], axis=1, inplace=True)

#Number of inhabitants per plz
plz_einwohner_df = pd.read_csv('./Data/plz_einwohner.csv', sep=',', dtype={'plz': str, 'einwohner': int})
germany_plz_einwohner_df = pd.merge(left=germany_df, right=plz_einwohner_df, on='plz', how='left')
#print(germany_df.head())

fig, ax = plt.subplots()

germany_plz_einwohner_df.plot(ax=ax, column='einwohner', categorical=False, legend=True, cmap='autumn_r', alpha=0.8)

for c in top_cities.keys():
    ax.text(
        x=top_cities[c][0],
        y=top_cities[c][1] + 0.08,
        s=c,
        fontsize=12,
        ha='center',
    )

    ax.plot(
        top_cities[c][0],
        top_cities[c][1],
        marker='o',
        c='black',
        alpha=0.5
    )

ax.set(
    title='Germany: Number of Inhabitants per Postal Code',
    aspect=1.3,
    facecolor='lightblue'
)
plt.show()

#Price per sqm per PLZ
hk_cities_df = pd.read_csv('./Data/HK_cities.csv', sep=',', dtype={'plz': str})
hk_cities_df.groupby('plz')['price_sqm'].mean()
germany_price_sqm_df = pd.merge(left=germany_df, right=hk_cities_df, on='plz', how='left')
print(germany_price_sqm_df.head())

""" fig, ax = plt.subplots()

germany_price_sqm_df.plot(ax=ax, column='price_sqm', categorical=False, legend=True, cmap='autumn_r', alpha=0.8)

for c in top_cities.keys():
    ax.text(
        x=top_cities[c][0],
        y=top_cities[c][1] + 0.08,
        s=c,
        fontsize=12,
        ha='center',
    )

    ax.plot(
        top_cities[c][0],
        top_cities[c][1],
        marker='o',
        c='black',
        alpha=0.5
    )

ax.set(
    title='Germany: Mean price per sqm per Postal Code',
    aspect=1.3,
    facecolor='lightblue'
)
plt.show() """

#Price per sqm per PLZ in Hamburg
berlin_df = germany_price_sqm_df.query('ort == "Hamburg"')

fig, ax = plt.subplots()

berlin_df.plot(ax=ax, column='price_sqm', categorical=False, legend=True, cmap='autumn_r',)

ax.set(title='Hamburg: mean price per sqm per Postal Code', aspect=1.3, facecolor='lightblue')
plt.show()