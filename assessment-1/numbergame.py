n = int(input()) #5
arr = list(map(int, input().split())) #4 3 2 1 5
min_val = min(arr) # 1
max_val = max(arr) #5

if len(set(arr)) == (max_val-min_val+1): #5 == 5-1+1
    print("yes")
else:
    print("no")    