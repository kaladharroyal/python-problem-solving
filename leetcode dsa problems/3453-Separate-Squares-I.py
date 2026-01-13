class Solution:
    def separateSquares(self, squares: list[list[int]]) -> float:
        low = float('inf')
        high = float('-inf')
        total = 0.0

        # Find search range and total area
        for x, y, l in squares:
            low = min(low, y)
            high = max(high, y + l)
            total += l * l

        target = total / 2.0

        # Binary search on y-coordinate
        for _ in range(100):
            mid = (low + high) / 2.0
            area = 0.0

            for x, y, l in squares:
                if mid <= y:
                    continue
                elif mid >= y + l:
                    area += l * l
                else:
                    area += l * (mid - y)

            if area < target:
                low = mid
            else:
                high = mid

        return (low + high) / 2.0
Solution.separateSquares([])