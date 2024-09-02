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
person_dict = {}

# %%
person_dict
# %%
person_dict['name'] = "Arie"
# %%
person_dict["city"] = "Emmen"
person_dict["hobbies"] = ['sport', 'chess', 'programming']
person_dict["age"] = 40
person_dict["pet"] = "Winston"


# %%
person_dict
# %%
person_dict["city"] = "Terschelling"


#%%
person_dict['pet']
# %%
person_dict.keys()
# %%
person_dict.values()

# %%
family = []

person_1 = {"name": "James"}
person_2 = {"name": "Mary"}

# %%
family.append(person_1)
family.append(person_2)
family.append(person_dict)

# %%
family

# %%
len(family)
# %%
family[-1]['hobbies'][-2:][-1][:2]
# %%
