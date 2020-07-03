class myQueue:
  def __init__(self):
    self.elements = []
  def isEmpty(self):
    if len(self.elements)==0:
      return True
    else:
      return False
  def enqueue(self,element):
    self.elements.append(element)
  def dequeue(self):
    return self.elements.pop(-1)    #pop the last element of the queue(ie:the most right child)
