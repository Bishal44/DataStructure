"""
Datastructure_and_algorithm
Created by Bishal on 24 Mar 2020
"""


# invert a binary tree

def reverse(root):
    if root is None:
        return
    root.left, root.right = root.right, root.left
    if root.left:
        reverse(root.left)
    if root.right:
        reverse(root.right)