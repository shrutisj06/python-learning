#converting tuple into list
countries = ("Spain", "Italy", "India", "England", "Germany")
temp=list(countries)
temp.append("indonesia")
temp[2]=("France")
counries=tuple(temp)

print(temp)


#concatenate two tuples
countries = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
countries2 = ("Vietnam", "India", "China")
southEastAsia = countries + countries2
print(southEastAsia)

#count
Tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2,5)
print(Tuple1.count(2))

#index
print(Tuple1.index(5))

#index in particular range
print(Tuple1.index(3,2,9))
