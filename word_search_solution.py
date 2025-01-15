class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # totalChars is the board flattened into a linear list for ease of traversal when checking for a characters existence within the board
        totalChars, visited, word = [item for sublist in board for item in sublist], [], list(word)
        
        # traverse the word and return False if any of the characters are not present in the board
        for char in word:
            if char not in totalChars:
                return False

        def backtrack(y, x, chars, visited):

            # if chars is empty, the word has been formed with the current path so return True
            if not chars:
                return True
            
            # check if the coordinates are in bound, unvisited, and that the current character is the next character in the word, otherwise return False
            if not (0 <= y < len(board) and 0 <= x < len(board[0]) and [x]+[y] not in visited and board[y][x] == chars[0]):
                return False
            chars = chars[1:]

            # if any recursive calls to the four surrounding nodes return True, return True
            if backtrack(y, x+1, chars, visited+[[x]+[y]]) or backtrack(y-1, x, chars, visited+[[x]+[y]]) or backtrack(y, x-1, chars, visited+[[x]+[y]]) or backtrack(y+1, x, chars, visited+[[x]+[y]]):
                return True

        # traverse the board linearly and call backtrack on the nodes whose character matches the first character of the word
        for y, row in enumerate(board):
            for x, char in enumerate(row):
                if char == word[0]:
                    ret = backtrack(y, x, word, visited)
                    if ret:
                        return ret

        # if no return statement has been reached, return False
        return False
