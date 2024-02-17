#lists
lst1=["blue","red","black","white"]
print(lst1)
print(lst1[3])#printing indexes

# a single list can contain items of different data types
details=["shruti","student",19,"female",6/6]
print(details)

colors = ["Red", "Green", "Blue", "Yellow", "Green"]
print(colors[-2]) #printing negative indexes
print(colors[-1])

check whether an item is present in the list or not?
if "Green" in colors:
     print("yes")
else:
     print("no")

#range of index
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[3:8])
print(animals[-8:-2])
print(animals[ : :2])
print(animals[ :])


#list comprehension
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
nameswith_s=[item for item in names if "s" in item]
print(nameswith_s)
