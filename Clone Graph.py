# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def __init__(self):
        self.dict = {}
        
    def cloneGraph(self, node):
        # write your code here
        def dfs(input,map):
            if input in map:
                return map[input]
            output=UndirectedGraphNode(input.label)
            map[input]=output
            for neighbour in input.neighbors:
                output.neighbors.append(dfs(neighbour,map))
            return output

        if node==None:
            return None
        return dfs(node,{})