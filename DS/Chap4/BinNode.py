#长子兄弟表示法：父节点指向first child，且first child指向next sibling
#利用长子兄弟表示法，二叉树能表示所有类型的树
class BinNode:
    def __init__(self,data,parent = None):
        self.parent = parent
        self.lChild = None
        self.rChild = None
        self.data = data
        self.height = 0

    def size(self):
        s = 1
        if self.lChild is not None:
            s += self.lChild.size()
        if self.rChild is not None:
            s += self.rChild.size()
        return s

    def insertAsLC(self,e):
        '''作为左孩子插入新节点'''
        newnode = BinNode(e,self)
        self.lChild = newnode
        return newnode

    def insertAsRC(self,e):
        '''作为右孩子插入新节点'''
        newnode = BinNode(e,self)
        self.rChild = newnode
        return newnode

    def __str__(self):
        st = " "*3 + str(self.data)+"\n"
        if self.lChild is not None and self.rChild is not None:
            st += " "*2+"/"+" "*2+"\\"+"\n"
            st += str(self.lChild.data)+" "*4 + str(self.rChild.data)
        elif self.lChild is not None:
            st += " " * 2 + "/" + "\n"
            st += str(self.lChild.data)
        elif self.rChild is not None:
            st += " "*5 + "\\"+"\n"
            st += " "*6 + str(self.rChild.data)
        return st

    def succ(self):
        '''中序意义下，当前节点的直接后继'''
        pass

if __name__ == '__main__':
    tree = BinNode(15)
    tree.insertAsLC(12)
    tree.insertAsRC(15)
    print(tree)