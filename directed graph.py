class GraphD:
    def __init__(self, n):
        self.M = [[0] * n for _ in range(n)]

    def insertEdge(self, s, t):
        if s < len(self.M[0]) and t < len(self.M[0]):
            self.M[s][t] = 1

    def delEdge(self, s, t):
        if s < len(self.M[0]) and t < len(self.M[0]):
            self.M[s][t] = 0

    def bfs(self, start):
        visited = [False] * len(self.M)
        queue = [start]
        visited[start] = True
        print("BFS path:", end=" ")
        while queue:
            node = queue.pop(0)
            print(node, end=" ")
            for i in range(len(self.M[node])):
                if self.M[node][i] == 1 and not visited[i]:
                    queue.append(i)
                    visited[i] = True
        print()

    def dfs(self, start, visited=None):
        if visited is None:
            visited = [False] * len(self.M)
        print(start, end=" ")
        visited[start] = True
        for i in range(len(self.M[start])):
            if self.M[start][i] == 1 and not visited[i]:
                self.dfs(i, visited)

    def display(self):
        print("Directed Graph Matrix:")
        for row in self.M:
            print(row)