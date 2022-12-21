#张雨佳 陈诗韵 黄卓然
from Array1D import*
class AssassinNode:
  def __init__(self,name):
    self.name=name
    self.target=None
    self.killer=None

class AssassinManager:
  def __init__(self,namelist):
    self.head=AssassinNode(namelist.pop(0))
    node=self.head
    while len(namelist)>0:
      node.target=AssassinNode(namelist.pop(0))
      node.target.killer=node
      node=node.target
    node.next=self.head
    node.next.killer=node
    self.gravelist=list()
      
  def kill(self,name):
    node=self.head
    while node.name !=name and node is not self.head.killer:
      node=node.target
    if node.name==name:
      node.target.killer=node.killer
      node.killer.target=node.target
      if node==self.head:
        self.head=node.target
      self.gravelist.append(node,name)

  def printGraveYard():
    for i in range(len(gravelist)):
      print(str(gravelist[i].name))

  def killRingContains(self,name):
    node=self.head
    while node.name !=name and node.target is not self.head:
      node=node.target
    if node.name==name:
      return True
    return False

  def graveYardContains(self,name):
    return name in self.gravelist

   
  def win():
    if gameOver() is True:
      return self.head
    return str("Null")

  def gameOver():
    if self.head.target is self.head:
      return True
    return False   
