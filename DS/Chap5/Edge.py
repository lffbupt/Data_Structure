from enum import Enum

class EStatus(Enum):
    UNDETERMINED = 0
    TREE = 1
    CROSS = 2
    FORWARD = 3
    BACKWARD = 4

class Edge:
    def __init__(self,data = None,weight = None,status = EStatus.UNDETERMINED):
        self.data = data
        self.weight = weight
        self.status = status