#邻接矩阵表示图
import Chap3.Queque as Queque
class Gragh:
    def __init__(self, V=[], E=[]):
        self.V = V
        self.E = E

    def BFS(self,v,clock):
        Q = Queque.Queque()


