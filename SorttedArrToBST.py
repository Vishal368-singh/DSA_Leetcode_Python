class Treenode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.val = data
def insert(left,right):
    if left>right:
        return None
    mid = (left + right)//2
    node = Treenode(nums[mid])
    node.left = insert(left,mid-1)
    node.right = insert(mid+1,right)
    return node
nums = [int(nums) for nums in input("Enter the array :").split(',')]
print("Original array is : ",nums)
BST =insert(0, len(nums)-1)
#Print the tree
def print_in_order(root):
    if root:
        print_in_order(root.left)
        print(root.val, end=' ')
        print_in_order(root.right)
print("BST in-order traversal:")
print_in_order(BST)