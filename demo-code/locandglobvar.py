y=20
def fun2():
    x=10
    global z 
    z = 30
    # This declares z as a global variable
    print(f"inside the function z= {z}")
    # The following line will raise an error because x is a local variable
    print(f"inside the function x = {x}")
fun2()
print(f"outside the function z = {z}")  # This will work because z is defined in the global scope
print(f"outside the function y = {y}")  # This will work because y is defined in the global scope
# The following code demonstrates the use of local and global variables in Python.
# this is accessing a local variable of a function 
# print(f"outside the function x = {x}")  # This will raise an error because x is not defined outside the function