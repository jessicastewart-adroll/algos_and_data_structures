'''Reverse a singly linked list.'''
class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None
    
class LinkedList(object):
  def __init__(self):
    self.head = None
