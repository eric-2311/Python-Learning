def num_teams(rating):
    import pdb
    # pdb.set_trace()
    teams = 0
    l = []
    x = 0

    while x <= len(rating)-2:
        y = x + 1
        while y <= len(rating)-1:
            z = y + 1
            while z < len(rating):
                if rating[x] < rating[y] and rating[y] < rating[z]:
                    teams += 1
                    l.append([rating[x], rating[y], rating[z]])
                elif rating[x] > rating[y] and rating[y] > rating[z]:
                    teams += 1
                    l.append([rating[x], rating[y], rating[z]])

                z += 1
            y += 1
        x += 1

    
    print(l)
    print(teams)



rating = [2,5,3,4,1] # 3 because [2, 3, 4], [5, 4, 1], [4, 3, 2]
# num_teams(rating)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        depth = 1
        check = root
        
        print(root)
        
        if root == None:
            return 0
        elif root.left and root.right == None:
            return 2
        elif root.right and root.left == None:
            return 2
        
        while check.right != None and check.left != None:
            if check.left.left == None and check.left.right == None:
                check = check.right
                depth += 1
                self.maxDepth(check)
            elif check.right.right == None and check.right.left == None:
                check = check.left
                depth += 1
                self.maxDepth(check)
            elif check.left.left and check.left.right == None:
                check = check.left
                depth += 1
                self.maxDepth(check)
            elif check.left.left == None and check.left.right:
                check = check.right
                depth += 1
                self.maxDepth(check)
            elif check.right.left and check.right.right == None:
                check = check.left
                depth += 1
                self.maxDepth(check)
            elif check.right.right and check.right.left == None:
                check = check.right
                depth += 1
                self.maxDepth(check)
                
        print(depth)
        
p = Solution()
l = TreeNode([1,2,3,4,None,None,5])
p.maxDepth(l)