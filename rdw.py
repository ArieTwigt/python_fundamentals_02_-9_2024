#%%
import requests
import pandas
import sys


# %% #"90ljkk"
#plate = input("Voer kenteken in:\n")
#plate_upper = plate.upper()
#endpoint = f"https://opendata.rdw.nl/resource/m9d7-ebf2.json?kenteken={plate_upper}"

brand = input("Voer merk in:\n")
brand_upper = brand.upper()
endpoint = f"https://opendata.rdw.nl/resource/m9d7-ebf2.json?merk={brand_upper}&$limit=150000"


# %%
response = requests.get(endpoint)

# %%
response.status_code

# %%
cars_list =  response.json()

if len(cars_list) == 0:
    print(f"❌ No cars found for {brand}")
    sys.exit()


# %%
len(cars_list)
# %%
print(cars_list[0]['merk'])
print(cars_list[0]['handelsbenaming'])


# %%
cars_df = pandas.DataFrame(cars_list)
# %%
cars_df.to_csv(f"{brand}.csv")
# %%
