# This program says hello and asks for your name.


print('Hello world!')
print('What is your name?')  # asks for name input
myName = input()
print('It is good to meet you, ' + myName)
print('The length of your name is: ')
print(len(myName))
print('What is your age?')   # asks for age input
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')
