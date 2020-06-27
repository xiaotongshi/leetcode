# 前序遍历
def PreOrder(self, root):
    '''打印二叉树(先序)'''
    if root == None:
        return 
    print(root.val, end=' ')
    self.PreOrder(root.left)
    self.PreOrder(root.right)

# 中序遍历
def InOrder(self, root):
    '''中序打印'''
    if root == None:
        return
    self.InOrder(root.left)
    print(root.val, end=' ')
    self.InOrder(root.right)

# 后序遍历
def BacOrder(self, root):
    '''后序打印'''
    if root == None:
        return
    self.BacOrder(root.left)
    self.BacOrder(root.right)
    print(root.val, end=' ')

# 宽度优先遍历
def BFS(self, root):
    '''广度优先'''
    if root == None:
        return
    # queue队列，保存节点
    queue = []
    # res保存节点值，作为结果
    #vals = []
    queue.append(root)

    while queue:
        # 拿出队首节点
        currentNode = queue.pop(0)
        #vals.append(currentNode.val)
        print(currentNode.val, end=' ')
        if currentNode.left:
            queue.append(currentNode.left)
        if currentNode.right:
            queue.append(currentNode.right)
    #return vals

# 深度优先遍历
def DFS(self, root):
    '''深度优先'''
    if root == None:
        return
    # 栈用来保存未访问节点
    stack = []
    # vals保存节点值，作为结果
    #vals = []
    stack.append(root)

    while stack:
        # 拿出栈顶节点
        currentNode = stack.pop()
        #vals.append(currentNode.val)
        print(currentNode.val, end=' ')
        if currentNode.right:
            stack.append(currentNode.right)
        if currentNode.left:
            stack.append(currentNode.left)			
    #return vals