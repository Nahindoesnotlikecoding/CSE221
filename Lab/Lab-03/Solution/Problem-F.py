def problem_F(inorder, preorder):
    if len(inorder)<1 or len(preorder)<1:
        return []
    
    root = preorder[0]
    
    root_index = inorder.index(root)
    
    left_postorder = problem_F(inorder[:root_index], preorder[1:1+root_index])
    
    right_postorder = problem_F(inorder[root_index+1:], preorder[root_index+1:])
    
    return left_postorder + right_postorder + [root]

def solve():
    n = int(input())
    inorder = list(map(int, input().split()))
    preorder = list(map(int, input().split()))
    postorder = problem_F(inorder, preorder)
    for i in postorder:
        print(i, end=" ")

solve()