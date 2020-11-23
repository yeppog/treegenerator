class BstNode:
    
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None

    def insert(self, key):
        if self.key == key:
            return
        elif self.key < key:
            if self.right is None:
                self.right = BstNode(key)
            else:
                self.right.insert(key)
        else: # self.key > key
            if self.left is None:
                self.left = BstNode(key)
            else:
                self.left.insert(key)

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.key
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.key
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

def constructInPost(start, end, postorder, pIndex, dict):
     
    # base case
    if start > end:
        return None, pIndex
 
    # Consider the next item from the end of given postorder sequence
    # This value would be the root node of subtree formed by inorder[start, end]
    root = BstNode(postorder[pIndex])
    pIndex = pIndex - 1
 
    # search the index of current node in inorder sequence to determine
    # the boundary of left and right subtree
    index = dict[root.key]
 
    # recursively construct the right subtree
    root.right, pIndex = constructInPost(index + 1, end, postorder, pIndex, dict)
 
    # recursively construct the left subtree
    root.left, pIndex = constructInPost(start, index - 1, postorder, pIndex, dict)
 
    # return root node
    return root, pIndex

def constructTreeInPost(inorder, postorder):
     
    # get size
    n = len(inorder)
 
    # dict is used to efficiently find the index of any element in
    # given inorder sequence
    dict = {}
    for i, e in enumerate(inorder):
        dict[e] = i
 
    # pIndex stores the index of next unprocessed node from the end
    # of postorder sequence
    pIndex = n - 1
    return constructInPost(0, n - 1, postorder, pIndex, dict)[0]

def constructPreIn(start, end, preorder, pIndex, dict):
     
    # base case
    if start > end:
        return None, pIndex
 
    # The next element in preorder will be the root node of subtree
    # formed by inorder[start, end]
    root = BstNode(preorder[pIndex])
    pIndex = pIndex + 1
 
    # get the index of root node in inorder to determine the
    # boundary of left and right subtree
    index = dict[root.key]
 
    # recursively construct the left subtree
    root.left, pIndex = constructPreIn(start, index - 1, preorder, pIndex, dict)
 
    # recursively construct the right subtree
    root.right, pIndex = constructPreIn(index + 1, end, preorder, pIndex, dict)
 
    # return current node
    return root, pIndex
 
 
# Construct a binary tree from inorder and preorder traversals
# This function assumes that the input is valid
# i.e. given inorder and preorder sequence forms a binary tree
def constructTreePreIn(inorder, preorder):
 
    # create a dictionary to efficiently find the index of any element in
    # given inorder sequence
    dict = {}
    for i, e in enumerate(inorder):
        dict[e] = i
 
    # pIndex stores index of next unprocessed node in preorder sequence
    # start with root node (present at 0'th index)
    pIndex = 0
 
    return constructPreIn(0, len(inorder) - 1, preorder, pIndex, dict)[0]



if __name__ == '__main__':
    
    def inpost (inorder, postorder):
        root = constructTreeInPost(inorder, postorder)
        root.display()

    def prein (inorder, preorder):
        root = constructTreePreIn(inorder, preorder)
        root.display()


    restart = True
    while restart:
        while restart:
            toggle = input("1. Preorder Inorder \n2. Inorder Postorder")
            if toggle == str(1):
                inorder = (input("Input inorder sequence \n")).split(" ")
                preorder = (input("Input preorder sequence \n")).split(" ")
                try:
                    prein(inorder, preorder)
                except: 
                    print("Something went wrong, check your sequence?")
                    break
            elif toggle == str(2):
                inorder = (input("Input inorder sequence \n")).split(" ")
                postorder = (input("Input postorder sequence \n")).split(" ")
                try:
                    inpost(inorder, postorder)
                except: 
                    print("Something went wrong, check your sequence? \n")
                    break
            else:
                print("Dont be a fucking idiot \n")
                break

            end = input("Quit? Y for Yes N for No \n")
            if (end.lower() == "y"):
            
                restart = False
                
            else:
                break
            


