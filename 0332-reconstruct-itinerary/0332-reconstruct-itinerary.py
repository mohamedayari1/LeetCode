class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = collections.defaultdict(list)

        for from_node, to_node in tickets:
            adj[from_node].append(to_node)

        for key in adj:
            adj[key].sort(reverse=True)

        result = []
        def dfs(node):
            while adj[node]: #Checking if the list of node's neighbors is still not empty 
                to_node = adj[node].pop()
                dfs(to_node)
            result.append(node)

        dfs("JFK")
        return result[::-1]