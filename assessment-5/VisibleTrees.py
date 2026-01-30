n = int(input())
arr = list(map(int, input().split()))
max_height = -1
visible = []
for height in arr:
    if height > max_height:
        visible.append(height)
        max_height = height
print(*visible)         
