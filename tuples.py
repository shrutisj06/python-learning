#tuple introduced with () brackets
tuple1=(44,3,5,7,8)
print(tuple1)
print(type(tuple1))

#can store diferent datatypes in single tuple
tuple2=(55,"shruti",True,88.3)
print(tuple2)

#tuple indexing(positive)
tuple2=(55,"shruti",True,88.3)
print(tuple2[3])
print(tuple2[0])

#negative indexing
country = ("Spain", "Italy", "India", "England", "Germany")
print(country[-2])
print(country[-5])

#check if a given item is present in the tuple.
country = ("Spain", "Italy", "India", "England", "Germany")
if "Italy" in country:
    print("yyes")
else:
    print("no")

#: Printing elements within a particular range:
animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[2:8]) #positive indexes
print(animals[-8:-2]) #negative indexes

#Printing all element from a given index till the end
print(animals[1:]) #positive
print(animals[-1:]) #negative

#print alternate values
print(animals[0:9:2])
print(animals[0:9:3])
