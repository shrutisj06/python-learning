english={1:50,2:35,3:0,4:45}
hindi={10:34,12:45,7:50}

#update
english.update({1:49})
print(english)

#clear
hindi.clear()
print(hindi)

#pop
english.pop(3)
print(english)

#pop item
english.popitem()
print(english)

#del
del english[1]
print(english)

del english
print(english)
