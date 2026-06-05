class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # need to return a list of all the cells that can flow into both the pacific and atlantic
        # return a list of all cells where there is a path from current cell to the top/left and the bottom/right
        # return a list of all cells where there is path such that set of neighboring cells less than or equal curr, where curr is defined recursively, such that, that set contains at least 1 cell with index [0,x] or [x,0], and 1 cell with index [m-1, x] or [x, n-1]

        # So could just do BFS, DFS. No need for something like A* probably, and at each step check the stack, until there are no elements in the stack left or we meet the conditions

        # Oh wait, I need to check EVERY square
        # ok, so there is a diagonal from [0, n-1] to [m-1,0] where any paths to the corners have to pass
        # initalize a set at [0, n-1] and check its neighbors BFS getting larger, if there are none bigger and it runs out, move to the next diagonal? 
            # thats actually not quite right, 
            # Start at the corners and add anything SMALLER
            # Then go along the diagonal adding all items to the stack that ARENT in the set yet
            # So set would contain their row major index maybe? row-major index: for a given square [i,j], row-major index = m*i + j, where m is the len(heights)
        # Oh wait, that assumes that the island is always a square
        # Instead, will need some way to link up the diagonals
        # If it is m x n, then goes right m/n elements and up n/m elements each step (round up?) (don't like it, adds a lot of edge cases)
        # m/n is the gradient, so if it goes through that square at all we add it, so yes round up
        # That means we need to search 

        # So the full psuedocode algorithm:
        # add all the diagonals to stack
        # while stack:
            # curr = stack.pop()
            # curr_stack = [curr]
            # curr_path_to_edge = False
            # while curr_stack:
                # if curr in path_to_edge: 
                    # curr_path_to_edge = true
                    # continue

        # wait hang on, theres still elements where it won't be able to path to the edge
        # No I can get this to work, so if an element is in the current stack

        # Ok so search just along the diagonal first
        # then keep track of all elements where it goes UP from there in that loop
        # So if our starting element is [3,3] for this loop, look at all neighbors, append the HIGHER OR EQUAL neighbors to the stack outside the loop
        # The lower neighbors can just be used as pathing, include them into current stack until the curr_stack is empty or we reach both oceans
        
        # That will work, because for an element to reach both oceans, it needs to cross the diagonal.
        # And to cross the diagonal means you have to be equal to or greater than in height than it
        # hardest part is still getting the mid.
        # Could literally just do the whole pacific wall? Has to be crossed? 
        
        # ok better strat, simpler => bfs or dfs from the coast just go up and make a set pacific_reachable, and make a set atlantic_reachable

        pacific_reachable = set()
        atlantic_reachable = set()

        # do pacific reachable first
        stack = []
        height = len(heights)
        width = len(heights[0])
        for i in range(width):
            stack.append((0, i))
        for i in range(height):
            stack.append((i, 0))
        
        print(stack)

        def BFS(curr):
            if curr[0]<height-1 and heights[curr[0]][curr[1]] <= heights[curr[0]+1][curr[1]]:
                stack.append((curr[0]+1, curr[1]))
            
            if curr[0]>0 and heights[curr[0]][curr[1]] <= heights[curr[0]-1][curr[1]]:
                stack.append((curr[0]-1, curr[1]))
            
            if curr[1] < width-1 and heights[curr[0]][curr[1]] <= heights[curr[0]][curr[1]+1]:
                stack.append((curr[0], curr[1]+1))
            if curr[1]>0 and heights[curr[0]][curr[1]] <= heights[curr[0]][curr[1]-1]:
                stack.append((curr[0], curr[1]-1))
        
        while stack:
            curr = stack.pop()
            if curr in pacific_reachable:
                continue
            pacific_reachable.add(curr)
            BFS(curr)
   
        # now do atlantic_reachable
        for i in range(width):
            stack.append((height-1, i))
        for i in range(height):
            stack.append((i, width-1))
        
        while stack:
            curr = stack.pop()
            if curr in atlantic_reachable:
                continue
            atlantic_reachable.add(curr)
            BFS(curr)

        both = atlantic_reachable & pacific_reachable

        return_list = []
        for item in both:
            return_list.append(list(item))

        return return_list

    # So I already had to get help for this
    # It is decent now, but repeating a lot of code now.
    # also BFS is wrong (its DFS) and the code is very brittle

    def pacificAtlanticBetter(self, heights: List[List[int]]) -> List[List[int]]:
        def dfs(r, c, reachable_set):
            if (r,c) in reachable_set:
                return
            height = len(heights)-1
            width = len(heights[0])-1
            reachable_set.add((r,c))

            if r < height and heights[r+1][c] >= heights[r][c]:
                dfs(r+1, c, reachable_set)
            if c < width and heights[r][c+1] >= heights[r][c]:
                dfs(r,c+1, reachable_set)

            if r > 0 and heights[r-1][c] >= heights[r][c]:
                dfs(r-1,c, reachable_set)
            if c > 0 and heights[r][c-1] >= heights[r][c]:
                dfs(r,c-1, reachable_set)



        pacific_reachable = set()
        atlantic_reachable = set()

        height = len(heights)
        width = len(heights[0])
        for i in range(width):
            dfs(0, i, pacific_reachable)
            dfs(height-1, i, atlantic_reachable)
        for i in range(height):
            dfs(i, 0, pacific_reachable)
            dfs(i, width-1, atlantic_reachable)
        
        both = atlantic_reachable & pacific_reachable

        return_list = []
        for item in both:
            return_list.append(list(item))

        return return_list

    # Better, but 
    # 1) calculating height and width in the loop=>redundant, do it outside and pass values in
    # 2) For loop at the bottom to return the list is dumb, do it better => more pythonic

    def pacificAtlanticOptimal(self, heights: List[List[int]]) -> List[List[int]]:
        def dfs(r, c, reachable_set, height, width):
            if (r,c) in reachable_set:
                return
            reachable_set.add((r,c))

            if r < height and heights[r+1][c] >= heights[r][c]:
                dfs(r+1, c, reachable_set, height, width)
            if c < width and heights[r][c+1] >= heights[r][c]:
                dfs(r,c+1, reachable_set, height, width)

            if r > 0 and heights[r-1][c] >= heights[r][c]:
                dfs(r-1,c, reachable_set, height, width)
            if c > 0 and heights[r][c-1] >= heights[r][c]:
                dfs(r,c-1, reachable_set, height, width)



        pacific_reachable = set()
        atlantic_reachable = set()

        height = len(heights)
        width = len(heights[0])
        for i in range(width):
            dfs(0, i, pacific_reachable, height-1, width-1)
            dfs(height-1, i, atlantic_reachable, height-1, width-1)
        for i in range(height):
            dfs(i, 0, pacific_reachable, height-1, width-1)
            dfs(i, width-1, atlantic_reachable, height-1, width-1)
        
        both = atlantic_reachable & pacific_reachable

        return [list(cell) for cell in both]
