"""
Datastructure_and_algorithm
Created by Bishal on 25 Mar 2020
"""
def max_path_sum(root):
    maximum = float("-inf")
    helper(root, maximum)
    return maximum


def helper(root, maximum):
    if root is None:
        return 0
    left = helper(root.left, maximum)
    right = helper(root.right, maximum)
    maximum = max(maximum, left+right+root.val)
    return root.val + maximum