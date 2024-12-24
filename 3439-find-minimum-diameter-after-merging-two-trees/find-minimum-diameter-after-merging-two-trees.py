from typing import List
class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        n1, n2 = len(edges1) + 1, len(edges2) + 1
        graph1, graph2 = [[] for _ in range(n1)], [[] for _ in range(n2)]
        
        for u, v in edges1:
            graph1[u].append(v)
            graph1[v].append(u)
            
        for u, v in edges2:
            graph2[u].append(v)
            graph2[v].append(u)
            
        self.dia = -1
        visited1 = [False] * n1
        self.getDia(0, graph1, visited1)
        d1 = self.dia
        
        self.dia = -1
        visited2 = [False] * n2
        self.getDia(0, graph2, visited2)
        d2 = self.dia
        
        cand = (d1 + 1) // 2 + (d2 + 1) // 2 + 1
        return max(cand, max(d1, d2))

    def getDia(self, src: int, graph: List[List[int]], visited: List[bool]) -> int:
        visited[src] = True
        dch, sdch = -1, -1
        
        for child in graph[src]:
            if not visited[child]:
                ch = self.getDia(child, graph, visited)
                if ch > dch:
                    sdch, dch = dch, ch
                elif ch > sdch:
                    sdch = ch
                    
        if dch + sdch + 2 > self.dia:
            self.dia = dch + sdch + 2
        return dch + 1