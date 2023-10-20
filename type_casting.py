# type casting simply means changing one datatypes to another datatypes

n1= input('enter 1 name : ')
n2= input('enter 2 name : ')
n3= input('enter 3 name : ')
n4= input('enter 4 name : ')

list = [n1,n2,n3,n4] # this line will display all your input
print(list) 

list = set(list) #change the type of the list
print(type(list)) # display the type of the list
print(list) #print the list
