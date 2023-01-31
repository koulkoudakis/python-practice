class TreeNode:
  def __init__(self, data, children = []):
    self.data = data
    self.children = children

  def __str__(self, level=0):
    ret = " " * level + str(self.data) + "\n"
    for child in self.children:
      ret += child.__str__(level + 1)
    return ret

  def addChild(self, TreeNode):
    self.children.append(TreeNode)

tree = TreeNode('Drinks', [])
cold = TreeNode('Cold', [])
hot = TreeNode('Hot', [])

tree.addChild(cold)
tree.addChild(hot)

# print(tree)

fanta = TreeNode('Fanta',[])
cola = TreeNode('Cola', [])
tea = TreeNode('Tea', [])
coffee = TreeNode('Coffee', [])

cold.addChild(fanta)
cold.addChild(cola)
hot.addChild(tea)
hot.addChild(coffee)

# print(tree)

# Binary tree using linked list


class TreeNode:
  def __init__(self, data):
    self.data = data
    self.leftChild = None
    self.rightChild = None

newBT = TreeNode("Drinks")
leftChild =  TreeNode("hot")
rightChild =  TreeNode("cold")

newBT.leftChild = leftChild
newBT.rightChild = rightChild

leftChildLeft = TreeNode("coffee")
leftChildRight = TreeNode("tea")

leftChild.leftChild = leftChildLeft
leftChild.rightChild = leftChildRight

def preOrderTraversal(rootNode):
  if not rootNode:
    return
  print(rootNode.data)
  preOrderTraversal(rootNode.leftChild)
  preOrderTraversal(rootNode.rightChild)

# preOrderTraversal(newBT)

def inOrderTraversal(rootNode):
  if not rootNode:
    return
  inOrderTraversal(rootNode.leftChild)
  print(rootNode.data)
  inOrderTraversal(rootNode.rightChild)

# inOrderTraversal(newBT)

def postOrderTraversal(rootNode):
  if not rootNode:
    return
  postOrderTraversal(rootNode.leftChild)
  postOrderTraversal(rootNode.rightChild)
  print(rootNode.data)

# postOrderTraversal(newBT)

import queue

def levelOrderTraversal(rootNode):
  if not rootNode:
    return
  else:
    customQueue = queue.Queue()
    customQueue.put(rootNode)
    while not(customQueue.empty()):
      root = customQueue.get()
      print(root.data)
      if (root.leftChild is not None):
        customQueue.put(root.leftChild)
        
      if (root.rightChild is not None):
        customQueue.put(root.rightChild)


# levelOrderTraversal(newBT)

def searchBT(rootNode, nodeValue):
  if not rootNode:
    return "The BT does not exist"

  else:
    customQueue = queue.Queue()
    customQueue.put(rootNode)
    while not(customQueue.empty()):
      root = customQueue.get()
      if root.data == nodeValue:
        return "Success"

      if root.leftChild is not None:
        customQueue.put(root.leftChild)

      if root.rightChild is not None:
        customQueue.put(root.rightChild)

    return "Value not found"

# print(searchBT(newBT, "tea"))  

def insertNodeBT(rootNode, newNode):
  print(newNode.data)
  if not rootNode:
    rootNode = newNode
  else:
    customQueue = queue.Queue()
    customQueue.put(rootNode)
    while not(customQueue.empty()):
      root = customQueue.get()
      
      if root.leftChild is not None:
        customQueue.put(root.leftChild)
        
      else:
        root.leftChild = newNode
        return f"{newNode.data} Successfully inserted"
        
      if root.rightChild is not None:
        customQueue.put(root.rightChild)
      else:
        root.rightChild = newNode
        return f"{newNode.data} Successfully inserted"

# newNode = TreeNode("cocoa")
# print(insertNodeBT(newBT, newNode))
# levelOrderTraversal(newBT)

# print(searchBT(newBT, "cocoa"))  

def getDeepestNode(rootNode):
  if not rootNode:
    return
  else:
    customQueue = queue.Queue()
    customQueue.put(rootNode)
    while not(customQueue.empty()):
      root = customQueue.get()
      if root.leftChild is not None:
        customQueue.put(root.leftChild)
        
      if root.rightChild is not None:
        customQueue.put(root.rightChild)

    deepestNode = root
    return deepestNode

# print(getDeepestNode(newBT).data)

    
def deleteDeepestNode(rootNode, dNode):
  if not rootNode:
    return
  else:
    customQueue = queue.Queue()
    customQueue.put(rootNode)

    while not(customQueue.empty()):
      root = customQueue.get()
      if root is dNode:
        root = None
        return "Node deleted"

      if root.rightChild is dNode:
        root.rightChild = None
        return "Node deleted"
      else:
        customQueue.put(root.rightChild)
        
      if root.leftChild is dNode:
        root.leftChild = None
        return "Node deleted"
      else: 
        customQueue.put(root.leftChild)


# newNode = getDeepestNode(newBT)
# deleteDeepestNode(newBT, newNode)
# # levelOrderTraversal(newBT)

# print(getDeepestNode(newBT).data)

def deleteNodeBT(rootNode, node):
  if not rootNode:
    return "The BT does not exist"
  else:
    customQueue = queue.Queue()
    customQueue.put(rootNode)
    while not(customQueue.empty()):
      root = customQueue.get()

      if root.data == node:
        dNode = getDeepestNode(rootNode)
        root.data = dNode.data
        deleteDeepestNode(rootNode, dNode)
        return "The node has been successfully deleted"

      if root.leftChild is not None:
        customQueue.put(root.leftChild)
      if root.rightChild is not None:
        customQueue.put(root.rightChild)
    return "Failed to delete node"

# print(deleteNodeBT(newBT, 'Drinks'))
# levelOrderTraversal(newBT)

def deleteBT(rootNode):
  rootNode.data = None
  rootNode.leftChild = None
  rootNode.rightChild = None

  return "The BT has been deleted successfully"

# deleteBT(newBT)
# levelOrderTraversal(newBT)


class BinaryTree:
  def __init__(self, size):
    self.customList = size * [None]
    self.lastUsedIndex = 0
    self.maxSize = size

  def insertNode(self, value):
    if self.lastUsedIndex + 1 == self.maxSize:
      return "The Binary Tree is full"
    self.customList[self.lastUsedIndex+1] = value
    self.lastUsedIndex += 1
    return "The value has been successfully inserted"

  def searchNode(self, nodeValue):
    for i in range(len(self.customList)):
      if self.customList[i] == nodeValue:
        return f"Successfully found {nodeValue} at {i}"
    return "Not found"

  def preOrderTraversal(self, index):
    if index > self.lastUsedIndex:
      return
    print(self.customList[index])
    self.preOrderTraversal(index*2)
    self.preOrderTraversal(index*2 + 1)

  def inOrderTraversal(self, index):
    if index > self.lastUsedIndex:
      return
    
    self.inOrderTraversal(index*2)
    print(self.customList[index])
    self.inOrderTraversal(index*2 + 1)
    
  def postOrderTraversal(self, index):
    if index > self.lastUsedIndex:
      return
    
    self.postOrderTraversal(index*2)
    self.postOrderTraversal(index*2 + 1)
    print(self.customList[index])

  def levelOrderTraversal(self, index):
    if index > self.lastUsedIndex:
      return

    for i in range(index, self.lastUsedIndex+1):
      print(self.customList[i])

  def deleteNode(self, value):
    if self.lastUsedIndex == 0:
      return "There is no node to delete"

    for i in range(1, self.lastUsedIndex+1):
      if self.customList[i] == value:
        self.customList[i] = self.customList[self.lastUsedIndex]
        self.customList[self.lastUsedIndex] = None
        self.lastUsedIndex -= 1
        return "Node has been successfully deleted"

  def deleteBT(self):
    self.customList = None
    return "The BT has been successfully deleted"
  

newBT = BinaryTree(8)
print(newBT.insertNode("Drinks"))
print(newBT.insertNode("Hot"))
print(newBT.insertNode("Cold"))
print(newBT.insertNode("Coffee"))


print(newBT.searchNode("Hot"))

# newBT.preOrderTraversal(1)
# newBT.inOrderTraversal(1)
# newBT.postOrderTraversal(1)
# newBT.levelOrderTraversal(1)

print(newBT.deleteNode("Hot"))
newBT.preOrderTraversal(1)

print(newBT.deleteBT())



  
        






      
      
  