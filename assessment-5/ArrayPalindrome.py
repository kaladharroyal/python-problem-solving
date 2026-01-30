n = int(input())
arr = list(map(int, input().split()))

if arr == arr[::-1]:
    print("True")
else:
    print("False")
