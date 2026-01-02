a = int(input("enter the number1 "))
b = int(input("enter the number2 "))
c = int(input("enter the number3 "))
root1 = (-b+(b**2-4*a*c)**0.5)/2*a
root2 = (-b-(b**2-4*a*c)**0.5)/2*a
print(f"the roots with values {a},{b},{c} is {root1},{root2}")
print(f"Roots({root1},{root2})")
