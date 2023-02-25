# Subject: functions and local/global variables
# This will be difficult !!!

# global variables
i = 0
print(i)
i = 100
print(i)

def fun1():
    i = 1 #local variable
    print(i)

# black line after function definition
def fun2():
    i = 10
    print(i)

fun1() #function call
fun2()
print(i)
