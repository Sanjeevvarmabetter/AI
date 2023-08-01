from collections import deque
class Solution:
    def bfstraversal(self,n,adj):
        bfs = []
        self.visited = [0] * n
        #we need to init queue as 0
        visited[0] = 1 #we are staring from 1
        q = deque()
        q.append(0)

        while queue: #this loop will traverse
            node = queue.popleft()
            bfs.append(node) 

        for i in adj[node]:
            if not visited[i]:
                q.append(i)
                visited[i] = 1   #we are marking the visited element as 1

        return bfs


    def addedge(self,adj,u,v):  #we are designing an adjacent matrix for our graph
        self.adj[u].append(v)
        self.adj[v].append(u)

    def printAns(ans)
        for i in range(len(ans)):
            print(ans[i],end = " ")

     
