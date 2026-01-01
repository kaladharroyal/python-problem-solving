from collections import Counter
s = input()
freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
print(freq)

print(max( freq, key = freq.get))