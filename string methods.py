name="shruti"
print(name[0:6])#using it to print stringa from a particular index to a particular index.

nm="harry"
print(nm[-4:-2])  #negative slicing

name1="shruti Jain"
print(name1.upper())  #for getting name in upper case use .upper()
print(name1.lower())  #for getting name in lower case use .lower()

print(name1.rstrip("Jain")) #strips the trailing characters

print(name1.replace("shruti","fruti")) #to replace a whole string with another
print(name1.split(" ")) #to split
print(name.capitalize())#to capitalize the first letter
print(name.center(60))#we have to specify by how many space we want to move it
print (len(name)) #to print length of string
print(name.count("shrutii"))
ss=("my name iss shruti")
print(ss)
print(ss.find("jain"))

namee="my nameis shruti"
print(namee.isprintable()) #returns true if printable false if not.

namee="my name is shruti\n"
print(namee.isprintable()) 

print(namee.isspace())
print(namee.istitle())
print(namee.title())
