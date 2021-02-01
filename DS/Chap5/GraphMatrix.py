import Chap3.Queque as Queque
import Chap5.Edge as Edge
import Chap5.Vertex as Vertex
class GraghMatrix:
    def __init__(self,V = [],E = []):
        self.V = V
        self.E = E
        self.e = 0
        self.n = 0
        self.clock = -1

    def vertex(self,i):
        return self.V[i].data

    def inDgree(self,i):
        return self.V[i].inDgree

    def outDgree(self,i):
        return self.V[i].outDgree

    def Vstatus(self,i):
        return self.V[i].status

    def dTime(self,i):
        return self.V[i].dTime

    def fTime(self,i):
        return self.V[i].fTime

    def parent(self,i):
        return self.V[i].parent

    def priority(self,i):
        return self.V[i].priority

    def nextBbr(self,i,j):
        j -= 1
        while(j>-1 and (not self.exist(i,j))):
            j -= 1
        return j

    def firstNbr(self,i):
        '''首个邻居'''
        return self.nextBbr(i,self.n)


    def exist(self,i,j):
        return (0<=i) and (i<self.n) and (0<=j) and (j<self.n) and (self.E[i][j] is not None)

    def edge(self,i,j):
        return self.E[i][j].data

    def Estatus(self,i,j):
        return self.E[i][j].status

    def weight(self,i,j):
        return self.E[i][j].weight

    def Einsert(self,edge,w,i,j):
        '''边插入'''
        if self.exist(i,j):
            return
        self.e += 1
        self.E[i][j] = Edge.Edge(edge,w)
        self.V[i].outDegree += 1
        self.V[j].inDegree += 1

    def Eremove(self,i,j):
        eBak = self.edge(i,j)
        del self.E[i][j]
        self.E[i][j] = None
        self.e -= 1
        self.V[i].outDegree -= 1
        self.V[j].inDegree -= 1
        return eBak

    def Vinsert(self,vertex):
        for i in range(self.n):
            self.E[i].append(None)
        self.n += 1
        newE = [None for j in range(self.n)]
        self.E.append(newE)

        newV = Vertex.Vertex(vertex)
        self.V.append(newV)
        return newV

    def Vremove(self,i):
        for j in range(self.n):
            if self.exist(i,j):
                del self.E[i][j]
                self.V[j].inDegree -= 1
        self.E.pop(i)
        self.n -= 1
        for j in range(self.n):
            if self.exist(j,i):
                del self.E[j][i]
                self.E[j].pop(i)
                self.V[j].outDegree -= 1
        vBak = self.vertex(i)
        self.V.pop(i)
        return vBak

    def BDS(self,v,clock=-1):
        Q = Queque.Queque()
        self.V[v].status = Vertex.VStatus.DISCOVERED
        Q.enqueue(v)
        while(Q.size != 0):
            v = Q.dequeue()
            clock += 1
            self.V[v].dTime = clock
            u = self.firstNbr(v)
            while(u>-1):
                us = self.V[u].status
                if us == Vertex.VStatus.UNDISCOVERED:
                    self.V[u].status = Vertex.VStatus.DISCOVERED
                    Q.enqueue(u)
                    self.E[v][u].status = Edge.EStatus.TREE
                    self.V[u].parent = v
                else:
                    self.E[v][u].status = Edge.EStatus.CROSS
                u = self.nextBbr(v, u)
            #print(self.V[v].data)
            self.V[v].status = Vertex.VStatus.VISITED

    def reset(self):
        for i in range(self.n):
            self.V[i].status = Vertex.VStatus.UNDISCOVERED
            self.V[i].dTime = -1
            self.V[i].fTime = -1
            self.V[i].parent = -1
            self.V[i].priority = float('inf')

            for j in range(self.n):
                if self.exist(i,j):
                    self.E[i][j].status = Edge.EStatus.UNDETERMINED


    def bfs(self,s):
        self.reset()
        clock = 0
        v = s
        i = 1
        while(True):
            if self.V[v].status == Vertex.VStatus.UNDISCOVERED:
                print("发现%d个连通阈..."%i)
                i += 1
                self.BDS(v,clock)
            v = (v+1) % self.n   #这里太牛了！！
            if v == s:
                break

    def DFS(self,v):
        self.clock += 1
        self.V[v].dTime = self.clock
        self.V[v].status = Vertex.VStatus.DISCOVERED
        print(self.V[v].data)
        u = self.firstNbr(v)
        while(u>-1):
            ustatus = self.V[u].status
            if ustatus == Vertex.VStatus.UNDISCOVERED:
                self.E[v][u].status = Edge.EStatus.TREE
                self.V[u].parent = v
                self.DFS(u)
            elif ustatus == Vertex.VStatus.DISCOVERED:
                self.E[v][u] = Edge.EStatus.BACKWARD
            else:
                if (self.V[v].dTime < self.V[u].dTime):
                    self.E[v][u] = Edge.EStatus.FORWARD
                else:
                    self.E[v][u] = Edge.EStatus.CROSS
            u = self.nextBbr(v,u)
        self.V[v].status = Vertex.VStatus.VISITED
        self.clock += 1
        self.V[v].fTime = self.clock

if __name__ == '__main__':
    G = GraghMatrix()
    # G.Vinsert("A")
    # G.Vinsert("B")
    # G.Vinsert("C")
    # G.Vinsert("D")
    # G.Vinsert("E")
    # G.Einsert(1, 1, 0, 2)
    # G.Einsert(1, 1, 2, 0)
    # G.Einsert(1, 1, 1, 0)
    # G.Einsert(1, 1, 0, 1)
    # G.Einsert(1, 1, 1, 3)
    # G.Einsert(1, 1, 3, 1)
    # G.Einsert(1, 1, 1, 2)
    # G.Einsert(1, 1, 2, 1)
    #G.bfs(0)
    #G.DFS(0)
    G.Vinsert("A")
    G.Vinsert("B")
    G.Vinsert("C")
    G.Vinsert("f")
    G.Vinsert("g")
    G.Einsert(1,1,0,1)
    G.Einsert(1,1,0,2)
    G.Einsert(1,1,0,3)
    G.Einsert(1,1,1,2)
    G.Einsert(1,1,3,4)
    G.Einsert(1,1,4,0)
    G.Einsert(1,1,4,2)
    G.DFS(0)
    for i in range(5):
        print("Node %d dTime and fTime"%i,G.V[i].dTime,G.V[i].fTime)


