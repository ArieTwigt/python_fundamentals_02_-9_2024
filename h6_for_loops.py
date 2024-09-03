#%% names list
names_list = ['arie', 'jim', 'bob']
names_list_upper = []

vowels = "aeoui"

for name in names_list:
    new_name = name.upper()

    if name[0] in vowels:
        names_list_upper.append(new_name)

# %%
names_list_upper



## Assignments

#%%
'''
Create a loop that removes the vowels from 
the following names list:
 ['Jim', 'John', 'Marc', 'Danny', 'Peter'] . 
Add the results to a new list.
'''

names_list =  ['Jim', 'John', 'Marc', 'Danny', 'Peter']
names_list_new = []

vowels = ('a', 'e', 'o', 'u', 'i', 'y')

for name in names_list:
    for letter in name:
        if letter.lower() in vowels:
            name = name.replace("letter", "")

    names_list_new.append(name)
    

names_list_new

# %%
'''
Create a loop that prints the name 
of the day for the following 10 days
'''

#%%
import datetime

# get the date of today
today_date = datetime.date.today()

max_days = 10 # set the limit
current_days = 1 # initate the value

while current_days <= max_days:
    new_date = today_date + datetime.timedelta(days=current_days)
    current_days += 1
    new_day_str = new_date.strftime("%A")
    print(new_day_str)

# %%
