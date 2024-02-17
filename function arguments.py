#default arguments
def average(a=6,b=10):
    average=(a+b)/2
    print(average)

average()

#keyword arguments

def name(good, better,best):
    print("my favorite fruit",good,better,best)

name(better = "apple", best = "mango", good = "guava")

#required arguments

def fruit(good,better,best):
    print("my favorite fruit",good,better,best)
fruit("guava","apple","mango")

#variable length

def name(*name):
    print("shruti",name[0],name[1],name[2])

name("ddd","frff","dde")
