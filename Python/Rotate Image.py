class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # idea: iterate over the outer square, in a 4 move pattern
        # So top left corner -> temp
        # bottom left -> top left
        # bottom right -> bottom left 
        # top right -> temp
        # let this 4 move pattern be called a set

        # then repeat this set for the whole top row
        # then repeat it for the next row down, minus the outer two (move two pointers in?)
        # Do this until the two pointers meet (will be at the middle)

        # So Iterate row-wise => top down, doing set rotation on all unswapped rows
        # This way we are rotating it in rings going inwards

        left = 0
        right = len(matrix) - 1
        n = len(matrix) - 1 # (0 indexed)
        row = 0

        def pixel_set_rotation(matrix, n, row, col):
            # input = top pixel in current set
            # need to take this, get the right col, bottom, and then left
            # top->left: x:row->col, y:col->row
            # top->bottom: x:row->n-row, y:col->n-col
            # top->right: x:row->col, y:col->n-row

            # so now we have the translated coordinates, need to start swapping
            # save top coordinate 
            temp = matrix[row][col]
            # then move left->top
            matrix[row][col] = matrix[n - col][row]
            # then move bottom->left
            matrix[n - col][row] = matrix[n - row][n - col]
            # then move right->bottom
            matrix[n - row][n - col] = matrix[col][n - row]
            # then save right=temp
            matrix[col][n - row] = temp

        # wont fire for bottom 2x2 for even matrices centers
        # will fire for center of odd matrices, but thats fine
        while left < right:
            for i in range(left, right):
                pixel_set_rotation(matrix, n, row, i)
            row += 1
            left += 1
            right -= 1
        return matrix



        
