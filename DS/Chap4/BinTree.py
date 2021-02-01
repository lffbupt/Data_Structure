import BinNode as BN
import Chap3.stack as Stack
import Chap3.Queque as Queque
class BinTree:
    def __init__(self,root = None):
        self.__root = root
        self.__size = 1
        self.value = []
        self.S = Stack.Stack()
        self.Q = Queque.Queque()

    def empty(self):
        return self.__root is None

    def root(self):
        return self.__root

    def size(self):
        return self.__size

    def stature(self,x):
        if x is None:
            return -1
        else:
            return x.height

    def updateHeight(self,x):
        '''更新节点x的高度'''
        x.height = max(self.stature(x.lChild),self.stature(x.rChild)) + 1
        return x.height

    def updateHeightAbove(self,x):
        '''更新节点x及祖先的高度'''
        while x is not None:
            UB = x.height
            if UB != self.updateHeight(x):
                x = x.parent
            else:
                break

    def insertAsLC(self,x,e):
        '''为x插入值为e的左节点'''
        newnode = BN.BinNode(e,x)
        x.lChild = newnode
        self.updateHeightAbove(x)
        self.__size += 1
        return newnode

    def insertAsRC(self,x,e):
        '''作为x插入值为e的右节点'''
        newnode = BN.BinNode(e,x)
        x.rChild = newnode
        self.updateHeightAbove(x)
        self.__size += 1
        return newnode

    #前序遍历，将右节点推入栈中
    def visitAlongLeftBranch(self,x):
        while(x is not None):
            self.value.append(x.data)
            if x.rChild is not None:
                self.S.push(x.rChild)
            x = x.lChild

    def travPre(self):
        '''子树先序遍历'''
        prob = self.__root
        while(True):
            self.visitAlongLeftBranch(prob)
            if self.S.size == 0:
                break
            prob = self.S.pop()

    #中序遍历
    def goAlongLeftBranch(self,x):
        while(x is not None):
            self.S.push(x)
            x = x.lChild

    def travIn(self):
        prob = self.__root
        while(True):
            self.goAlongLeftBranch(prob)
            if self.S.size == 0:
                break
            prob = self.S.pop()
            self.value.append(prob.data)
            prob = prob.rChild

    #层次遍历
    def travLevel(self):
        self.Q.enqueue(self.__root)
        while(self.Q.size != 0):
            prob = self.Q.dequeue()
            self.value.append(prob.data)
            if prob.lChild is not None:
                self.Q.enqueue(prob.lChild)
            if prob.rChild is not None:
                self.Q.enqueue(prob.rChild)


if __name__ == '__main__':
    #        12
    #       /  \
    #     12   15
    #    / \     \
    #  23  77    88
    #创建树：
    rootNode = BN.BinNode(12)
    tree = BinTree(root = rootNode)
    tree.insertAsLC(rootNode,12)
    tree.insertAsRC(rootNode,15)
    node1 = rootNode.lChild
    node2 = rootNode.rChild
    tree.insertAsLC(node1,23)
    tree.insertAsRC(node1,77)
    #print(node1)
    tree.insertAsRC(node2,88)
    #先序遍历
    # tree.travPre()
    # print("先序遍历：",tree.value)
    # print("根节点的深度：",rootNode.height)
    # print("第二层节点15的深度：",node2.height)
    # print("树的总节点数：",tree.size())
    #中序遍历
    tree.travIn()
    print("中序遍历：",tree.value)
    #层次遍历
    #tree.travLevel()
    #print("层次遍历：",tree.value)
