# the comparison operators are 

# > greater than
# >= greater than equal 
# < less than
# <= less than or equal to
# == equal to
# != not equal to

#heres an example 

name = input('Enter your name : ')
name = name.lower()

if name == 'maaz':
    print("Hello Maaz")
    food = 'Fried Rice'
elif name =='madni':
    print("hello madni")
    food = 'Rice'
else:
    print('you are not maaz , get out of here')

print(f'Your favourite food is {food}')
