from enum import Enum

class VStatus(Enum):
    UNDISCOVERED = 0
    DISCOVERED = 1
    VISITED = 2

class Vertex:
    def __init__(self,data = None,inDegree = 0,outDegree = 0,status = VStatus.UNDISCOVERED,dTime = -1,
                 fTime = -1,parent = -1,priority = float('inf')):
        self.data = data
        self.inDegree = inDegree
        self.outDegree = outDegree
        self.dTime = dTime
        self.fTime = fTime
        self.parent = parent
        self.priority = priority
        self.status = status
