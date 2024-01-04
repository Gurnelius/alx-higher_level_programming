#!/usr/bin/python3
'''
    Program that solves the N queens problem.
'''


import sys


class NQueensSolver:

    def __init__(self, N):
        """
        Initialize the NQueensSolver with the size of the chessboard.

        Parameters:
            N (int): The size of the chessboard and the number of queens.
        """
        self.validate_input(N)
        self.N = N
        self.board = [-1] * N

    def validate_input(self, N):
        """
        Validate the input provided for the size of the chessboard.

        Parameters:
            N (int): The size of the chessboard and the number of queens.

        Raises:
            ValueError: If N is not an integer.
            ValueError: If N is less than 4.
        """
        if not isinstance(N, int):
            raise ValueError("N must be a number")
        if N < 4:
            raise ValueError("N must be at least 4")

    def is_safe(self, row, col):
        """
        Check if placing a queen at the specified position is safe.

        Parameters:
            row (int): The row index.
            col (int): The column index.

        Returns:
            bool: True if safe, False otherwise.
        """
        for i in range(row):
            if self.board[i] == col or \
               self.board[i] - i == col - row or \
               self.board[i] + i == col + row:
                return False
        return True

    def solve_nqueens(self, row):
        """
        Recursively solve the N-Queens problem using backtracking.

        Parameters:
            row (int): The current row being considered.
        """
        if row == self.N:
            self.print_solution()
            return

        for col in range(self.N):
            if self.is_safe(row, col):
                self.board[row] = col
                self.solve_nqueens(row + 1)

    def print_solution(self):
        """
        Print the current solution in the specified format.
        """
        solution = [[i, self.board[i]] for i in range(self.N)]
        print(solution)

    def solve(self):
        """
        Solve the N-Queens problem and print all solutions.
        """
        self.solve_nqueens(0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens.py N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    try:
        solver = NQueensSolver(N)
        solver.solve()
    except ValueError as e:
        print(e)
        sys.exit(1)
