from collections import Counter
s1 = input()#aac
s2 = input() #abb

 # converts the string into the freqency dict
c1 = Counter(s1) #{'a':2, 'c':1}
c2 = Counter(s2) #{'a':1, 'b':2}

dele = 0

for ch in set(c1.keys()).union (c2.keys()):# unique from both strings {a,b}
    dele += abs(c1.get(ch, 0)-(c2.get(ch, 0))) # dele = 2-1
print(dele)    