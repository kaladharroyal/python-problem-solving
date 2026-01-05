class Solution:
    def maxMatrixSum(self, matrix: list[list[int]]) -> int:
        total_sum = 0        # Sum of absolute values
        neg_count = 0        # Count of negative numbers
        min_abs = float('inf')  # Smallest absolute value

        # Traverse every element in the matrix
        for row in matrix:
            for val in row:
                total_sum += abs(val)              # Add absolute value
                if val < 0:
                    neg_count += 1                 # Count negatives
                min_abs = min(min_abs, abs(val))   # Track smallest abs value

        # If negative count is odd, one value must stay negative
        if neg_count % 2 == 1:
            total_sum -= 2 * min_abs

        return total_sum
                
Solution.maxMatrixSum([[1, -1, 0], [-1, -1, -1], [0, -1, 1]])                