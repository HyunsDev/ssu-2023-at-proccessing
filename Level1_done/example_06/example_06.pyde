# Subject: print() function to print something on the console

print("Hello World")
print(1)
print("My name is Ben")
print("print function is useful when you are debugging")
print("you can see your program's running status by printing some informaiton")  

# operator precendence 
print(3 * 2 + 4) # good
# better to use space before and after the operator
print(3*2+4) # bad

print(3 + 2 * 4)
print(3+2*4)

print(3 + 2 - 4) 
print(3+2-4)

# these are called 'literal'
print(1, 2) # integer literal
print("Hello", "my name is Ben") # string literal 

# variable and assignment operator
a = 10
print(a)

a = 30
print(a)

a = a + 20
print(a)

# In Processing.py, we can't use input() function.
# https://forum.processing.org/two/discussion/23646/how-to-use-input-with-python-processing-running-on-a-mac.html
a = input()
print(a)
