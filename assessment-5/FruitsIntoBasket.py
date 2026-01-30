n = int(input())
fruits = list(map(int, input().split()))

max_count = 0


for i in range(n):
    basket = set()
    count = 0

    for j in range(i, n):
        basket.add(fruits[j])

        if len(basket) > 2:
            break

        count += 1

    max_count = max(max_count, count)

print(max_count)