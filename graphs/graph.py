from collections import defaultdict as dd



class Graph:
    
    def __init__(self):
        self.graph = dd(list)

    def add_edge(self, u,v):
    
        self.graph[u].append(v)

    def BFS(self,s):
        print(f"BFS that start with vertex {s}")

        lVisited = [False] * (max(self.graph) + 1)
        lQueue = []

        lQueue.append(s)
        lVisited[s] = True
        
        
        while(lQueue):

            s = lQueue.pop(0)            
            print(s, end= " ")
            for child in self.graph[s]:
                if lVisited[child] == False:
                   lQueue.append(child)
                   lVisited[child]= True


#Driver code

g = Graph()
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(1,2)
g.add_edge(2,0)
g.add_edge(2,3)
g.add_edge(3,3)

print(g.graph)

g.BFS(2)
