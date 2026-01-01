n = int(input().strip())
s = input().strip()
v = "aeiouAEIOU"
count = 0
for ch  in s[:n]:
    if ch.isalpha() and ch not in v:
        count+=1
print(count)            