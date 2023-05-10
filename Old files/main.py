import pandas as pd
import matplotlib.pyplot as plt

hk_cities = pd.read_csv('./Data/HK_cities.csv')

df = pd.DataFrame(hk_cities)

df_filtered_energiequsweistyp = df[df['energieeffizienzklasse'] != 'Not specified']
print(df_filtered_energiequsweistyp['energieeffizienzklasse'].head())

df['adat_year'] = df['adat'].astype(str).str[:4]
#count_by_year = df.groupby('adat_year').size()
#print(count_by_year)

average_price_sqm_per_year = df.groupby('adat_year')['price_sqm'].mean()
#print(average_price_sqm_per_yer)
plt.plot(average_price_sqm_per_year.index, average_price_sqm_per_year.values)
plt.xlabel("Year")
plt.ylabel('Mean price per Square Meter')
plt.title('Mean Price per Square Meter for House Purchases per Year')
plt.show()


plz_city = pd.read_csv('./Data/zuordnung_plz_ort.csv')
df_plz_city = pd.DataFrame(plz_city)

merged_df = pd.merge(df, df_plz_city, on="plz")

big_cities = ['Hamburg', 'Hannover', 'Bremen', 'Düsseldorf', 'Essen', 'Duisburg', 'Köln', 'Dortmund', 'Frankfurt', 'Stuttgart', 'München', 'Nürnberg', 'Berlin', 'Dresden', 'Leizig']
filtered_df = merged_df[merged_df['ort'].isin(big_cities)]

count_by_ort = filtered_df.groupby('ort')['price_sqm'].count()
print(count_by_ort)

plt.bar(count_by_ort.index, count_by_ort.values)
plt.xlabel("City")
plt.ylabel('Mean price per Square Meter')
plt.title('Mean Price per Square Meter for House Purchases per City')
plt.show()
