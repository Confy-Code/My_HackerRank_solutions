# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''
def height(root):
    
    if not root:
        return 0
    
    if not root.left and not root.right:
        return 0
        
    root.left = height(root.left) + 1
    root.right = height(root.right) + 1
    
    return max(root.left, root.right)