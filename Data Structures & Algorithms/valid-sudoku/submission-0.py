class Solution:
    
    _empty: str = "."

    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_size = len(board)
        global_cols_count = [{} for _ in range(row_size)]
        sub_board_count = [{} for _ in range(row_size)]

        if(row_size % 3) != 0: return False

        for row_index,row in enumerate(board):
            if len(row) != row_size: return False
            count_row = {}
            for col_index,col in enumerate(row):
                if col == self._empty: continue
                count_row[col] = count_row.get(col,0) + 1
                current_global_count = global_cols_count[col_index]
                current_global_count[col] = current_global_count.get(col,0) + 1

                sub_board_index = row_index // 3 * 3 + col_index // 3
                current_sub_board_count = sub_board_count[sub_board_index]
                current_sub_board_count[col] = current_sub_board_count.get(col,0) + 1


            count_row_sorted = sorted(count_row.values())
            if len(count_row_sorted) > 0 and count_row_sorted[0] > 1: return False

        has_col_greater_than_one = any(
            value > 1
            for d in global_cols_count
            for value in d.values()
        )

        has_sub_board_greater_than_one = any(
            value > 1
            for d in sub_board_count
            for value in d.values()
        )

        if has_col_greater_than_one or has_sub_board_greater_than_one: return False

        return True      


                            






        
        