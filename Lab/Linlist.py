class LinkNode:
  def __init__(self,data):
    self.data = data
    self.next = None

  def __str__(self):
    return str(self.data)+ "-->"

class Linklist:
  def __init__(self):
    self.head=None

  def find(self,target):
    node=self.head
    while(node is not None):
      if(node.data==target):
        return node
      else:
        return None
  def add(self,data):
    node=LinkNode(data)
    node.next=self.head #self.head全称它指的东西
    self.head=node

  def remove(self,data):
    pre =None
    node = self.head
    while(node is not None and note.data!=data):
      pre=node
      node= node.next
    
    if node is not None:  
      if (node is self.head):
        self.head = node.next
      else:
         self.next=pre.next


  def __iter__(self):
    return LinkIT(self,head)

class LinkIT:
  def __init__(self,head):
    self.node=head

  def __iter__(self):
    return self
 
  def __next__(self):
    if self.node is None:
      raise StopIteration
    else:
      node=self.node
      self.node=self.node.next
      return node

if __name__=="__main__" :
  l=Linklist()
  l.add('a')
  l.add('blah') 
