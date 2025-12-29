# ---------- Sudoku Solver ----------
class Sudoku:
    def __init__(self, board):
        self.board = board

    def is_valid(self, row, col, num):
        for i in range(9):
            if self.board[row][i] == num or self.board[i][col] == num:
                return False
        start_row, start_col = 3*(row//3), 3*(col//3)
        for i in range(3):
            for j in range(3):
                if self.board[start_row+i][start_col+j] == num:
                    return False
        return True

    def solve(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:
                    for num in range(1, 10):
                        if self.is_valid(row, col, num):
                            self.board[row][col] = num
                            if self.solve():
                                return True
                            self.board[row][col] = 0
                    return False
        return True

    def print_board(self):
        for row in self.board:
            print(row)
        print()


# ---------- 8 Queens ----------
class EightQueens:
    def __init__(self):
        self.board = [[0]*8 for _ in range(8)]

    def safe(self, row, col):
        for i in range(row):
            if self.board[i][col] == 1:
                return False
        i, j = row-1, col-1
        while i>=0 and j>=0:
            if self.board[i][j] == 1:
                return False
            i -= 1
            j -= 1
        i, j = row-1, col+1
        while i>=0 and j<8:
            if self.board[i][j] == 1:
                return False
            i -= 1
            j += 1
        return True

    def solve(self, row=0):
        if row == 8:
            self.print_board()
            return True
        for col in range(8):
            if self.safe(row, col):
                self.board[row][col] = 1
                if self.solve(row+1):
                    return True
                self.board[row][col] = 0
        return False

    def print_board(self):
        for row in self.board:
            print(row)
        print()


# ---------- Count Islands ----------
class Islands:
    def __init__(self, matrix):
        self.matrix = matrix

    def dfs(self, i, j):
        if i<0 or i>=len(self.matrix) or j<0 or j>=len(self.matrix[0]) or self.matrix[i][j]==0:
            return
        self.matrix[i][j] = 0
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        for di,dj in dirs:
            self.dfs(i+di,j+dj)

    def count_islands(self):
        count = 0
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                if self.matrix[i][j]==1:
                    self.dfs(i,j)
                    count += 1
        return count


# ---------- DFS in Binary Tree ----------
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = root

    def dfs(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return
        print(node.val)
        self.dfs(node.left)
        self.dfs(node.right)


# ---------- Example Usage ----------
if name == "__main__":
    # Sudoku example
    sudoku_board = [
        [5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]
    ]
    sudoku = Sudoku(sudoku_board)
    sudoku.solve()
    sudoku.print_board()

    # 8 Queens example
    queens = EightQueens()
    queens.solve()

    # Count islands example
    matrix = [
        [1,1,0,0],
        [0,1,0,0],
        [0,0,1,1],
        [1,0,0,1]
    ]
    islands = Islands(matrix)
    print("Number of islands:", islands.count_islands())

    # Binary tree DFS example
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.
    right = Node(5)
    tree = BinaryTree(root)
    print("DFS of binary tree:")
    tree.dfs()
