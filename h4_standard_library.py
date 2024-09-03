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
type(folder_name)


# Assignments

# Assignment
'''
Assign a variable that holds the 
number of days until your next birthday
'''

# %% a. 
birthday_date = date(2025, 2, 26)
birth_until_birthday = birthday_date - date.today() 
print(birth_until_birthday)



# %% b. 
'''
Calculate the surface 
of a circle with a diameter of 10 (radius^ * pi)
'''
import math

straal = 5
oppervlakte = math.pi * math.pow(straal, 2)
oppervlakte

# %% c.
'''
Create list that contains the 
files in your current working directory
'''
current_file_folders = os.listdir()
current_file_folders

# %% d.
'''
Add a directory with the name our_functions
'''
os.mkdir("our_functions")

#%%
os.makedirs("our_functions", exist_ok=True)

#%%
os.path.isdir('bmw.csv')

#%%
os.path.isdir('my_folder')
# %%
os.path.isfile('bmw.csv')
# %%
files = [x for x in current_file_folders if os.path.isfile(x)]
files
# %%
folders = [x for x in current_file_folders if not os.path.isfile(x)]
folders
# %%
