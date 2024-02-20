#union of sets
numbers={1,2,3,4,5,6,7,8}
numbers2={61,62,63,64,1,2,3}
print(numbers.union(numbers2))

#update
(numbers2.update(numbers))
print(numbers2)

#intersection
print(numbers.intersection(numbers2))

#update
(numbers.intersection_update(numbers2))
print(numbers)

#symmetric difference
(numbers.symmetric_difference(numbers2))
print(numbers)
#in update it will not make a new set just update the existing one

#difference and difference update
(numbers.difference(numbers2))
print(numbers)


#another set methods study from notebook


