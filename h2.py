server_name = "Server X"
# %%
#%%
server_name
# %%
user_age = 45
# %%
first_name = "Arie"
last_name = "Twigt"

first_name + last_name 
# %%
5 + 5
# %%
5 * first_name
# %%
True + True
# %%
True and False
# %%
print("Hello Arie")
# %%
print = "Arie"
# %%
print
# %%
print("Hello Arie")
# %%
my_list = ['Arie', 4000, True]
# %%
my_tuple = ('Arie', 4000, True)
# %%
my_tuple
# %%
my_list[1] = 5000
# %%
my_list
# %%
my_tuple[1] = 5000
# %%
my_tuple[0]

# %%
allowed_files = [".txt", ".csv"]

#%%
allowed_files = (".txt", ".csv")


#%% dictionary
person_dict = {"name": "Arie", 
               "age": 40,
               "hobbies": ['football', 'programming']}
# %%
person_dict['age']
# %%
person_list = ['Arie', 40, "Katwijk"]

#%% 
person_dict['hobbies']
# %%
person_dict['hobbies'][1]
# %%
my_list[3]
# %%
first_name
# %%
last_name
# %%
first_name + last_name
# %%
first_name + " " + last_name
# %%
f"Mijn voornaam is {first_name} en achternaam is {last_name}"

# %%
f"{first_name} {last_name}"

# %%
first_name + user_age
# %%
f"{first_name} {user_age}"
# %%
first_name.upper()
# %%
first_name.upper()
# %%
user_age.upper()
# %%
first_name.upper()
# %%
first_name.replace("r", "p")
# %%
my_list.append("✅")
# %%
my_list

# %%
first_name[0]

#%%
my_list[0]
# %%
person_dict['name']

# %%
first_name = "Arie"
last_name = "Twigt"
full_name = f"{first_name} {last_name}"
full_name

# %%
"{} {}".format(first_name, last_name)

# %%
first_letter = first_name[0]
first_letter
# %%
full_name_new = f"{first_letter}. {last_name}"
full_name_new


# Assignments

# Assignment 1

# %%
first_name = "Erling"
last_name  = "Haaland"

full_name  = first_name + last_name
print(full_name)

#  the format function
full_name = "{} {}".format(first_name, last_name)
print(full_name)

# %% a.
full_name + " Jr."

#%% b.
f"{full_name} .Jr"

append = "Jr"

full_name_new = f"{full_name} .{append}"


# Assignment 2.

# %% a.
full_name_new.replace("Erling", "E.")

# %% b.
first_letter = first_name[0]
f"{first_letter}. {last_name} {append}."

# %%
person_dict = {"name": "Arie"}


# %%
person_dict['name'][0]
# %%
names_list = ['Arie', 'James']

#%%
names_list[0][0]


# Assignment 3

#%%
'''
Create a variable called nationality with the value "Norway". 
Use this variable to create the string (sentence) 
"E. Haaland .Jr - Nationality: Norway". Print out the sentence.

'''

nationality = "Norway 🇳🇴"
f"{full_name_new} - Nationality: {nationality}"

# %%
# assignment
capital_append = append.capitalize() 

# evaluate
capital_append
# %%
