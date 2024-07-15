class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        """
        Tic-tac-toe is played by two players A and B on a 3 x 3 grid. The rules of Tic-Tac-Toe are:

        Players take turns placing characters into empty squares ' '.
        The first player A always places 'X' characters, while the second player B always places 'O' characters.
        'X' and 'O' characters are always placed into empty squares, never on filled ones.
        The game ends when there are three of the same (non-empty) character filling any row, column, or diagonal.
        The game also ends if all squares are non-empty.
        No more moves can be played if the game is over.
        Given a 2D integer array moves where moves[i] = [rowi, coli] indicates that the ith move will be played on grid[rowi][coli]. 
        return the winner of the game if it exists (A or B). In case the game ends in a draw return "Draw". If there are still movements to play return "Pending".

        You can assume that moves is valid (i.e., it follows the rules of Tic-Tac-Toe), the grid is initially empty, and A will play first.
        """

        def wins(moves: List[List[int]]) -> bool:
            # rows
            if [0, 0] in moves and [0, 1] in moves and [0, 2] in moves: return True
            if [1, 0] in moves and [1, 1] in moves and [1, 2] in moves: return True
            if [2, 0] in moves and [2, 1] in moves and [2, 2] in moves: return True

            # columns
            if [0, 0] in moves and [1, 0] in moves and [2, 0] in moves: return True
            if [0, 1] in moves and [1, 1] in moves and [2, 1] in moves: return True
            if [0, 2] in moves and [1, 2] in moves and [2, 2] in moves: return True

            # diagonal
            if [0, 0] in moves and [1, 1] in moves and [2, 2] in moves: return True
            if [2, 0] in moves and [1, 1] in moves and [0, 2] in moves: return True
            
            return False 

        if wins([n for n in moves[::2]]): return "A"
        if wins([n for n in moves[1::2]]): return "B"
        if len(moves) < 9: return "Pending"
        return "Draw"
