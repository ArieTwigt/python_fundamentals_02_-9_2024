#%% name
name = "Arie"
list(name)

# %%
my_list = []

#%%
my_list.append("Arie")
# %%
my_list
# %%
my_list.remove("Arie")
# %%
my_list
# %%
# %%
my_list.append("Dirk")
# %%
my_list
# %%
numbers_list = [1,2,3,4,5]
letters_list = ['a', 'b', 'c', 'd', 'e']

numbers_list + letters_list

#%%
4 + "Arie"
# %%
letters_list_2 = ["b", "a", "g", "z", "f"]
sorted(letters_list_2)
# %%
letters_list = ['a', 'a', 'b', 'c']
# %%
letters_list_unique = list(set(letters_list))
type(letters_list_unique)
# %%
letters_list_unique

#%%
letters_list = ['a', 'b', 'c', 'd', 'e']
letters_list_2 = ['f', 'g', 'h', 'i', 'j']

# %%
letters_list.append(letters_list_2)

#%%
letters_list

#%%
letters_list = letters_list + letters_list_2
# %%
letters_list[5][0]

#%%
letters_list = ['a', 'b', 'c', 'd']

# %%
'''
['a', 'b', 'c', 'd']
  0    1    2    3
 -4    -3   -2   -1

'''

#%%

#%%
last = len(letters_list) - 1
letters_list[last]
# %%
letters_list[-3]
# %%
letters_list[1:]
# %%
letters_list[-2:]
# %%
letters_list[1:2]
# %%
letters_list[2:4]
# %%

# %%
prices_list = [0.5, 1.25, 3.75]
prices_list[2] # <- integer

# %%
person_3 = {}

# %%
person_3
# %%
person_3['name'] = "Arie"
# %%
person_3["city"] = "Emmen"
person_3["hobbies"] = ['sport', 'chess', 'programming']
person_3["age"] = 40
person_3["pet"] = "Winston"


# %%
person_3
# %%
person_3["city"] = "Terschelling"


#%%
person_3['pet']
# %%
person_3.keys()
# %%
person_3.values()

# %%
family = []

person_1 = {"name": "James"}
person_2 = {"name": "Mary"}

# %%
family.append(person_1)
family.append(person_2)
family.append(person_3)

# %%
family

# %%
len(family)
# %%
family[-1]['hobbies'][-2:][-1][:2]
# %%


# Assignments

'''
Create a dictionary with an (imaginary) person with attributes like his name, age and hobbies
'''

#%%
person_1 = {"name": "Dirk",
            "age": 40,
            "hobbies": ["sport", "gaming", "reading"]}

# %%
person_2 = {"name": "Mary",
            "age": 44,
            "hobbies": ["tennis", "cooking", "reading"]}

person_3 = {"name": "Bobby",
            "age": 14,
            "hobbies": ["football", "racing", "programming"]}


#%% a.
family_list = [person_1, person_2, person_3]
family_list

# %%
family_dict = {}
family_dict['name'] = "Jones"
family_dict['members'] = [person_1, person_2, person_3]
family_dict

# %%
family_dict['members'][-1]['hobbies'][1]
# %%
