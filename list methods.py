#list methods

#sort no.in ascending order
numbers=[6,7,5,9,2,3,1000,2]
numbers.sort()
print(numbers)

#sort no. in descending order
numbers.sort(reverse=True)
print(numbers)

#reverse
numbers.reverse()
print(numbers)

#index of number
print(numbers.index(2))

#count
print(numbers.count(2))

#copy
num=numbers.copy()
print(num)

#append
numbers.append(2004)
print(numbers)

#insert
numbers.insert(5,10000)
print(numbers)

#extend
numbers.extend(num)
print(numbers)

#concatenating two lists
print(numbers+num)
