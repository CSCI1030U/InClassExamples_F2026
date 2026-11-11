def solve_n_queens(n):
    # start with empty board
    state = [["."] * n for _ in range(n)]
    solutions = []
    
    # which columns already have a queen?
    visited_cols = set()
    
    # which diagonals already have a queen?
    visited_diagonals = set()
    
    # which perpendicular diagonals already have a queen?
    visited_antidiagonals = set()
    
    def backtrack(row):
        if row == n:
            solutions.append(["".join(row) for row in state])
            return
        
        for col in range(n):
            diag = row - col
            anti_diag = row + col
            
            # if the current square doesn't have another queen in same column and diagonal
            if not (col in visited_cols or diag in visited_diagonals or anti_diag in visited_antidiagonals):                    
                # remember which column and diagonals this space occupies
                visited_cols.add(col)
                visited_diagonals.add(diag)
                visited_antidiagonals.add(anti_diag)

                # place the queen at row,col
                state[row][col] = 'Q'

                # try to put a queen on the next row
                backtrack(row + 1) 

                # reset the visited lists
                visited_cols.remove(col)
                visited_diagonals.remove(diag)
                visited_antidiagonals.remove(anti_diag)
                
                # reset the board
                state[row][col] = '.'

    backtrack(0)

    return solutions

def print_solution(index, solution):
    result = f'Solution {index + 1}: '
    for row in solution:
        result += row + ' '
    print(result)

solutions = solve_n_queens(8)
for index in range(len(solutions)):
    print_solution(index, solutions[index])
