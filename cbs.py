#%%
import requests
import pandas

endpoint = "https://opendata.cbs.nl/ODataApi/odata/70262ENG/UntypedDataSet"

#%%

response = requests.get(endpoint)

data = response.json()
#%%
data_df = pandas.DataFrame(data['value'])


print(data)
# %%
