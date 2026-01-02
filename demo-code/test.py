#expected_output = "Hello, John!"
"""a = input("enter name :")
print("Hello,"+a+"!")
#expected_output = you entered 5
b = int(input("Enter the number"))
print("You have entered:",b,sep="")
"""
#input 10 20 30 
#output 60
"""a=input()
x,y,z= a.split(" ")#splits the input string into three parts
print(int(x)+int(y)+int(z))
"""
#input john, 25
#output Name: john, Age: 25
"""
inp = input("enter name and age")
name,age=inp.split(",")
print("Name:"+name+", Age:",age ,sep=" ")"""
#ormatting output
x,y = input("enter name and age  ").split(",")
print(f"name:{x},age: {y} years old")