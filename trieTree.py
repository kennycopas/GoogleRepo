# trieNode class holds two values:
#   val = the current character
#   pointers = list of child nodes (auto-populated with None 26 times, one index for each letter of the alphabet)
class trieNode:
    def __init__(self, val):
        self.val = val
        self.pointers = [None] * 26

# Simple calculation that takes a character and returns an int n such that the character is the nth letter of the alphabet
toNum = lambda char: ord(char) - ord('a')

# createPath takes a string input and the root node and creates a path of nodes where each node is a character of the string
def createPath(input, root):
    curNode = root
    for i, char in enumerate(input):
        # For each character in the string input,
        # if the current node (the previous character) has no pointer to the current character,
        # create a node and make a pointer to that node using the toNum indexing
        if curNode.pointers[toNum(char)] is None:
            curNode.pointers[toNum(char)] = trieNode(char)
        curNode = curNode.pointers[toNum(char)]
