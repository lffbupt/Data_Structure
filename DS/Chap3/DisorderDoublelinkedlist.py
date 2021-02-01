#无序链表
#有序链表
class Node:
    def __init__(self,value = None):
        self.value = value
        self.pred = None
        self.succ = None

class Doublelinkedlist:
    def __init__(self):
        self.__header = Node()#哨兵
        self.__tailer = Node()#哨兵
        self.__header.succ = self.__tailer
        self.__tailer.pred = self.__header
        self.size = 0

    def __isEmpty(self):
        return(self.size == 0)

    #循秩访问
    def __getitem__(self, item):
        if self.__isEmpty():
            return None
        elif item < 0 or item >= self.size:
            raise IndexError
        else:
            prob = self.__header
            cur = -1
            while cur<item:
                prob = prob.succ
                cur += 1
            return prob.value

    #查找,节点p的n个真前躯中（不包含p）是否有某个特定的值e,若有则返回该节点
    def __find(self,e,n,p):
        p = p.pred
        while (n > 0 and p != self.__header):
            if e == p.value:
                return p
            n -= 1
            p = p.pred
        return None

   #插入，ac，在c前插入节点b，即abc
    def insertBefore(self,pos,e):
        '''insertBefor(pos,e),在pos前插入节点e'''
        if pos<0 or pos > self.size:
            raise IndexError

        newNode = Node(e)
        if self.__isEmpty():
            self.__header.succ = newNode
            newNode.pred = self.__header
            newNode.succ = self.__tailer
            self.__tailer.pred = newNode
            self.size += 1
        else:
            cur = -1
            prob = self.__header
            while(cur < pos):
                prob = prob.succ
                cur += 1
            pre = prob.pred
            pre.succ = newNode
            newNode.pred = pre
            newNode.succ = prob
            prob.pred = newNode
            self.size += 1

    #删除某节点，并返回删除值
    def __remove(self,prob):
        pre = prob.pred
        after = prob.succ
        pre.succ = after
        after.pred = pre
        self.size -= 1
        e = prob.value
        del prob
        return e

    #删除某元素
    def remove(self,pos):
        if pos < 0 or pos >= self.size:
            raise  IndexError
        if self.__isEmpty():
            return None
        else:
            prob = self.__header
            cur = -1
            while(cur < pos):
                prob = prob.succ
                cur += 1
            pitem = prob.pred
            bitem = prob.succ
            pitem.succ = bitem
            bitem.pred = pitem
            e = prob.value
            self.size -= 1
            del(prob)
            return e

    #无序去重，返回被删除元素的总数
    def deduplicate(self):
        if self.size <2:
            return 0

        oldsize = self.size
        prob = self.__header.succ.succ
        newsize = 1
        while(prob != self.__tailer):
            e = prob.value
            q = self.__find(e,newsize,prob)
            if q is not None:
                self.__remove(q)
            else:
                newsize += 1
            prob = prob.succ
        return oldsize - newsize

    #有序链表去重
    def uniquify(self):
        if self.size < 2:
            return 0
        newsize = 1
        oldsize = self.size
        prob1 = self.__header.succ
        prob2 = prob1.succ
        while(prob2 != self.__tailer):
            if prob2.value != prob1.value:
                prob1 = prob2
                prob2 = prob1.succ
                newsize += 1
            else:
                self.__remove(prob2)
                prob2 = prob1.succ
        return oldsize - newsize

    def __str__(self):
        if self.__isEmpty():
            return "None"
        prob = self.__header.succ
        st = str(prob.value)
        while(True):
            prob = prob.succ
            if prob != self.__tailer:
                st = st + "->" + str(prob.value)
            else:
                break
        return st

    #选择排序，从交换次数的意义讲，此算法有很大的提高
    def __selctMax(self,p,n):
        '''selectMax(p,n):从起始于节点p的n个元素中选出最大者，包含p'''
        if n==1:
            return p
        max = p
        cur = p.succ
        while n > 1:
            if cur.value >= max.value:
                max = cur
            cur = cur.succ
            n -= 1
        return max

    def selectionsort(self):
        head = self.__header.succ
        tail = self.__tailer
        n = self.size
        i = 0
        while i<n:
            maxprob = self.__selctMax(head,n-i)
            temp = maxprob.value
            maxprob.value = tail.pred.value
            tail.pred.value = temp
            tail = tail.pred
            i += 1

    #插入排序
    #有序列表查找，在p的n个真前躯中（不包含p），找到不大于e的最后者
    def __search(self,e,n,p):
        p = p.pred
        while(n>0 and p!=self.__header):
            if p.value <= e:
                break
            n -= 1
            p = p.pred
        return p
    #在节点p后插入e
    def __insertAfter(self,p,e):
        newnode = Node(e)
        aft = p.succ
        p.succ = newnode
        newnode.pred = p
        newnode.succ = aft
        aft.pred = newnode
        self.size += 1

    def insertionsort(self):
        n = self.size
        if n < 2:
            pass
        sortedpos = 0
        prob = self.__header.succ
        while sortedpos < n:
            insertnode = self.__search(prob.value,sortedpos,prob)
            self.__insertAfter(insertnode,prob.value)
            prob = prob.succ
            self.__remove(prob.pred)
            sortedpos += 1



if __name__ == '__main__':
    Dll = Doublelinkedlist()
    for i in [1,1,2,4,7,8,7]:
        Dll.insertBefore(0,i)
    print(Dll)
    print("循秩访问第3个元素：",Dll[2])

    Dll.selectionsort()
    print("对无序列表排序：", Dll)
    print("*****************")
    m = Dll.deduplicate()
    print("删除了%d个元素"%m)
    print("无序去重后：",Dll)
    print("******************")
    sortlink = Doublelinkedlist()
    for j in [7,7,7,8,8,9,9,9,10,10]:
        sortlink.insertBefore(0,j)

    print("有序链表：",sortlink)
    n = sortlink.uniquify()
    print("删除了%d个元素"%n)
    print("有序去重后：",sortlink)

    print("*******************")
    orderlink = Doublelinkedlist()
    for z in  [4,2,7,13,20,1,33]:
        orderlink.insertBefore(0,z)
    print("无序链表：",orderlink)
    orderlink.insertionsort()
    print("插入排序：",orderlink)

    print("删除第一个元素：",orderlink.remove(0))
    print("删除后：",orderlink)



