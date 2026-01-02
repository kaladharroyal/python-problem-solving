"""import random,math
def generate_otp():
    otp = ""
    for i in range (6):
        a = random.random()
        b = math.floor(a*10)
        otp +=str(b)
    return otp

print("Your OTP is: ", generate_otp()) """
import random
a = random.randint(100000, 999999)
print("Your OTP is:", a)