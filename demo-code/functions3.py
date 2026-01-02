def get_max_min (numbers):
    return min(numbers), max(numbers)

nums = [10,20,30,40,50,60]
minimum, maximum = get_max_min(nums)
print(f"the minimum numbers is {minimum} and maximum number is {maximum}")