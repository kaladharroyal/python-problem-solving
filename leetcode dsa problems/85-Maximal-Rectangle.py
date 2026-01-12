class Solution:
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0

        cols = len(matrix[0])
        heights = [0] * (cols + 1)  # extra 0 as sentinel
        max_area = 0

        for row in matrix:
            # build histogram
            for i in range(cols):
                heights[i] = heights[i] + 1 if row[i] == "1" else 0

            # largest rectangle in histogram
            stack = []
            for i in range(cols + 1):
                while stack and heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, h * w)
                stack.append(i)

        return max_area
Solution.maximalRectangle = staticmethod(Solution.maximalRectangle)
# Example usage:
matrix = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"]
]
   