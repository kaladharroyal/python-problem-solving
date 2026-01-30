n = int(input())
piles = list(int, input().split())
h = int(input())

left = 1
right = max(piles)  
ans = right

while left <= right:
    mid = (left+right) //2
    hours = 0

    for piles in piles:
        hours += (piles + mid -1 ) // mid
        if hours <= h:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
print(ans)            