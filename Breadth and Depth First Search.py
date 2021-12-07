class Graph:
    def __init__(self):
        self.graph = {}
        
    def addEdge(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]
# Breadth First Search Algorithm
    def BFS(self, s):
        visited = [False] * len(self.graph)
        que = [s]
        visited[s] = True
        
        while len(que) > 0:
            s = que.pop(0)
            print(s)
            
            for node in self.graph[s]:
                if visited[node] == False:
                    que.append(node)
                    visited[node] = True
# Depth First Search Algorithm                   
    def DFS(self, s):
        visited = [False] * len(self.graph)
        stk = [s]
        visited[s] = True
        
        while len(stk) > 0:
            s = stk.pop()
            print(s)
            
            for node in self.graph[s]:
                if visited[node] == False:
                    stk.append(node)
                    visited[node] = True