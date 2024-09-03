#%%
age = 17
son_of_boss = False

if age > 18:
    print("You can have alcohol")
    print("Cheers")
elif son_of_boss: 
    print("Yes sir")
else:
    print("Unfortunately")

print("Anything else?")

# %%
guests_list = ['Bob', 'Arie', 'Jim']

person = "Dirk"

if person in guests_list:
    print("Welcome")
else:
    print("No")

# %%
name = "Arie"
letter = "a"

if letter in name.lower():
    print("Yes")
# %%

# %%
age = 17
son_of_boss = True


if age > 18 and son_of_boss:
    print("Special treatment")
elif son_of_boss:
    print("Yes sir")
elif age > 18:
    print("Yes")
else:
    print("No")


# %%
target_amount = 1000

donation_amount = 400

donated_amount = 0


while donated_amount < target_amount:
    print(f"Current amount {donated_amount}")
    donated_amount += donation_amount
    print(f"New amount {donated_amount}")


## Assignments

# %% 1. 
'''
Create a conditional statement that indicates if 
your name starts with an "A or not
'''

name = "Arie"

letter = "a"

if name[0].lower() == letter:
    print("Yes")

# %%
'''
Create a conditional statement that indicates 
if your name begins with a vowel. If it does, 
change it into a non-vowel and otherwise. 
For example: Arie –> Brie or Rose –> Aose

'''




# %%
name = "Arie"
first_letter = name[0]

vowels = ("a", "e", "o", "u", "i")

if first_letter.lower() in vowels:
    name = name.replace(first_letter, "B")
else:
    name = name.replace(first_letter, "A")



print(name)

# %% a. 
'''
Create a conditional statement that indicates 
if your age is between 18 and 68.
'''

age = 50

if age > 18 and age < 68:
    print("Yes")
else:
    print("No")



# %%
age = 70

if 18 < age < 68:
    print("Yes")
else:
    print("No")
# %%
