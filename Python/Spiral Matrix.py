class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # So is there a simple way to do this without keeping track of messy indicies?
        # So obviously add first row, then go down right row
        # This is still messy indicies tracking though
        # So treating the sub lists as lists:
        # Add first sublist in its entirety
        # pop last element off all sub matrices
        # add second sublist in its entirety
        # Wait this is wrong, has to be LAST sublist
        # so two pointer last and front to keep track of whats been added?
        # Just need one pointer, since it's mirrored 

        # Ok so this was entirely wrong, since its SPIRILING
        mat_out = []
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
        while top <= bottom and left <= right:
            # North: row = top, start = left, end = right
            for col in range(left, right + 1):
                mat_out.append(matrix[top][col])
            top += 1

            # East: col = right, start = top+1, end = bottom
            for row in range(top, bottom + 1):
                mat_out.append(matrix[row][right])
            right -= 1

            # South: row = bottom, start = right-1, end=left
            if top <= bottom:
                for col in range(right, left - 1, -1): 
                    mat_out.append(matrix[bottom][col])
                bottom -= 1 

            # West: col = left, start = bottom, end=top-1
            if left <= right:
                for row in range(bottom, top - 1, -1): 
                    mat_out.append(matrix[row][left])
                left += 1
        return mat_out
