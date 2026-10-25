"""
Given the following definition of a Node , please implement preorder traversal
https://en.wikipedia.org/wiki/Tree_traversal#Pre-order right inside Node. 
The sequence returned should be the sequence of values, not their containing nodes.
"""

from unittest import TestCase, TestLoader, TextTestRunner

class Node:
  def __init__(self, value, left=None, right=None):
    self.right = right
    self.left = left
    self.value = value

    self.parent = None

    if left:
      self.left.parent = self
    if right:
      self.right.parent = self

  def traverse_preorder(self):    
    
    yield self.value

    if self.left:
        yield from self.left.traverse_preorder()

    if self.right:
        yield from self.right.traverse_preorder()

class Evaluate(TestCase):
  def test_exercise(self):
    node = Node('a',
                Node('b',
                     Node('c'),
                     Node('d')),
                Node('e'))
    self.assertEqual(
      'abcde',
      ''.join([x for x in node.traverse_preorder()])
    )
 
if __name__ == "__main__":
    root = Node(1,
                Node(2),
                Node(3))

    for y in root.traverse_preorder():
      print(y, end=', ') # 1, 2, 3,

    suite = TestLoader().loadTestsFromTestCase(Evaluate)
    TextTestRunner().run(suite)