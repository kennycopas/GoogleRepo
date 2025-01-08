class brNode:
    def __init__(self, val):
        self.val = val
        self.black = False
        self.left = None
        self.right = None

# Recursive function that checks black counts on paths:
# recur():
# if node is None:
#     return count + 1
# elif node.black:
#     count += 1
# return recur(left, count) and recur(right, count)