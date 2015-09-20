# Definition for a Directed graph node
# class DirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    """
    @param graph: A list of Directed graph node
    @return: A list of integer
    """
    def topSort(self, graph):
        # write your code here
        def dfs():
