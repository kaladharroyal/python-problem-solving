import math
s = list(input().strip())
otp =""

for i, ch in enumerate(s):
    if i % 2 == 1:
        if ch.isdigit():
            otp += str(int(ch) ** 2)
        else:
            # skip non-digit characters at odd positions
            continue
if (len(otp)<4):
    print(-1)              
print(otp[:4])