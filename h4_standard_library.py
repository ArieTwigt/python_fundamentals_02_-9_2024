#%%
import math
from datetime import date, timedelta, datetime
import os

# %%


#%%
math.pow()

# %%
144 ** 0.5

#%%
pow()


#%%
christmast_date = date(2024, 12, 25)
# %%
today_date = date.today()
today_date
# %%
difference = christmast_date - today_date
# %%
difference.days

# %%
today_date + timedelta(days=50)

# %%
time_now = datetime.now()
time_now
# %%
lunch_time = datetime(2025, 12, 3, 12, 30, 0)

# %%
difference_time = lunch_time - time_now
difference_time

#%%
seconds_to_lunch = difference_time.seconds
seconds_to_lunch

# %%
time_now - timedelta(hours=3)

# %%
os.getcwd()

# %%
os.listdir()

# %%
os.mkdir("my_folder")

# %%
os.makedirs("my_folder/sub_folder", exist_ok=True)
# %%
os.makedirs("data/export/OPEL")
# %%
current_time = datetime.now()
current_time_str = current_time.strftime("%Y%m%d%H%M%S")
current_time_str

# %%
folder_name = f"export_{current_time_str}"
folder_name
# %%
os.mkdir(folder_name)
# %%
