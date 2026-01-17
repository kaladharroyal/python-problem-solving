n = 5

for i in range(n):
    # Print spaces for formatting
    print(" " * (n - i - 1), end="")
    
    # Print Pascal's triangle numbers
    for j in range(i + 1):
        if j == 0 or j == i:
            print(1, end=" ")
        else:
            # Calculate binomial coefficient
            val = 1
            for k in range(1, min(j, i - j) + 1):
                val = val * (i - k + 1) // k
            print(val, end=" ")
    
    print()  # New line after each row