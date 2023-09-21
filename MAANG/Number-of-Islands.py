'''Number of Islands
You are given a 2-D matrix surface of size n*m. Each cell of the surface is either 1 (land) or 0 (water).
Find the number of islands on the surface.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. Assume all four edges of the surface are all surrounded by water.

Example:
surface: [
 [1, 1, 0, 1]
 [1, 0, 1, 1]
 [0, 1, 0, 1]
]
Num islands: 3
Testing
Input Format
The first line contains an integer ‘T’ denoting the number of test cases.

For each test case the input has the following lines:

Two space-separated integers 'n' and 'm' denoting the number of rows and columns of the matrix.
n lines, each containing m space-separated integers denoting the elements of the matrix.
Output Format
For each test case, the output has a line containing the number of islands.

Sample Input
3
3 4
1 1 0 1
1 0 1 1
0 1 0 1
2 2
1 1
1 1
2 2
0 0
0 0
Expected Output
3
1
0
Constraints
1 <= T <= 10
1 <= n, m <= 200
0 <= surfaceij <= 1
Complete the below code as per the above question
class Solution:
	def getNumberOfIslands(self, surface: List[List[int]]) -> int:
		# add your logic here '''


class Solution:
    def getNumberOfIslands(self, surface: List[List[int]]) -> int:
        """
        Finds the number of islands in a given 2D matrix.

        Args:
            surface: A 2D matrix of integers, where 1 represents land and 0 represents water.

        Returns:
            The number of islands in the matrix.
        """

        # Initialize a visited matrix to keep track of which cells have already been visited.
        visited = [[False for _ in range(len(surface[0]))] for _ in range(len(surface))]

        # Initialize a count variable to store the number of islands found.
        count = 0

        # Iterate over the matrix.
        for i in range(len(surface)):
            for j in range(len(surface[0])):
                # If the current cell is land and has not been visited, start a DFS traversal from this cell.
                if surface[i][j] == 1 and not visited[i][j]:
                    self.dfs(surface, visited, i, j)
                    count += 1

        return count

    def dfs(self, surface, visited, i, j):
        """
        Performs a DFS traversal from the given cell, marking all connected land cells as visited.

        Args:
            surface: A 2D matrix of integers, where 1 represents land and 0 represents water.
            visited: A 2D matrix of booleans, where True indicates that the cell has been visited.
            i: The row index of the current cell.
            j: The column index of the current cell.
        """

        # Mark the current cell as visited.
        visited[i][j] = True

        # Check the four adjacent cells (up, down, left, and right) and perform a DFS traversal on each unvisited land cell.
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_i = i + dx
            new_j = j + d

            if 0 <= new_i < len(surface) and 0 <= new_j < len(surface[0]) and surface[new_i][new_j] == 1 and not visited[new_i][new_j]:
                self.dfs(surface, visited, new_i, new_j)


