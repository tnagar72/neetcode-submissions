class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9

        row_hashset = set()
        col_hashset = set()
        box_sets = [set() for _ in range(9)]


        for i in range(n):
            row_hashset = set()
            col_hashset = set()
            for j in range(n):
                row_val = board[i][j]
                col_val = board[j][i]

                if row_val != ".":
                    if row_val in row_hashset:
                        return False
                    else:
                        row_hashset.add(row_val)

                if col_val != ".":
                    if col_val in col_hashset:
                        return False
                    else:
                        col_hashset.add(col_val)

                box_col = ((i) // 3)
                box_row = ((j) // 3)

                if row_val != ".":
                    if row_val in box_sets[(box_row + (3 * box_col))]:
                        return False
                    else:
                        box_sets[(box_row + (3 * box_col))].add(row_val)

                
        return True



                

                
                


