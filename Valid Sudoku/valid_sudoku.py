class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Let's keep tracking each element and see where they belong
        """
        
        # Initialize tackers for each row, column and box
        row = {i: [] for i in range(9)}
        col = {i: [] for i in range(9)}
        box = {i: [] for i in range(9)}
        
        for i in range(9):
            for j in range(9):
                e = board[i][j]
                box_index = (i // 3) * 3 + j // 3
                
                if e == '.':
                    continue
                    
                if e in row[i] or e in col[j] or e in box[box_index]:
                    return False
                else:
                    row[i].append(e)
                    col[j].append(e)
                    box[box_index].append(e)
                    
        return True
