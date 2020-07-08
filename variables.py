

# Declare a variable and initialize it

# f=0
# print(f)

# re-declaring the variable also works

# f="abc"
# print(f)

# variables of different type cannot be combined
# cannot concatenate two different type of variable

# print("This is string" + 1)  # error
# print("This is string " + str(123))


# Global and local variables

# f=0

# def someFunction():
#     f="abc"
#     print(f)   # output abc


# someFunction()
# print(f)       # output: 0


# f=0

# def someFunction():
#     global f   # Here we told the function that f is global
#     f="abc"
#     print(f)   # output: abc


# someFunction()
# print(f)       # output: abc

f=0

def someFunction():
    global f   # Here we told the function that f is global
    f="abc"
    print(f)   # output: abc


someFunction()
print(f)       # output: abc

del f          # deletes the definition of the variable that was previously declared
print(f)       # error: name f is not defined