#无序列表的访问，平均而言是O（n）
class Node:
    def __init__(self,Value = None):
        self.value = Value
        self.nextNode = None

class LinkedList:
    def __init__(self):
        self.__head = None

    def isEmpty(self):
        return (self.__head is None)

    def items(self):
        if self.isEmpty():
            return
        prob = self.__head
        while prob is not None:
            yield prob.value
            prob = prob.nextNode

    def length(self):
        prob = self.__head
        cur = 0

        if self.isEmpty():
            return 0
        else:
            while prob is not None:
                cur += 1
                prob = prob.nextNode
        return cur

    def __add(self,value):
        newnode = Node(value)
        if self.isEmpty():
            self.__head = newnode
        else:
            newnode.nextNode = self.__head
            self.__head = newnode

    def append(self,value):
        newNode = Node(value)
        if self.isEmpty():
            self.__head = newNode
        else:
            prob = self.__head
            while prob.nextNode is not None:
                prob = prob.nextNode
            prob.nextNode = newNode
    #insert 3 in 1->4->23 at position 1,return 1->3->4->23
    def insert(self,pos,value):
        l_len = self.length()
        if (pos < 0) | (pos > l_len):
            print("pos输入错误")
            raise IndexError
        elif pos == 0:
            self.__add(value)
        elif pos == l_len:
            self.append(value)
        else:
            newNode = Node(value)
            prob = self.__head
            cur = 0
            while cur < pos:
                pre = prob
                prob = prob.nextNode
                cur += 1
            pre.nextNode = newNode
            newNode.nextNode = prob

    def remove(self,value):
        prob = self.__head
        pre = None

        while prob is not None:
            if prob.value != value:
                pre = prob
                prob = prob.nextNode
            else:
                if pre is not None:
                    pre.nextNode = prob.nextNode
                else:
                    self.__head = prob.nextNode
                return

    def find(self,value):
        return value in self.items()

    def __str__(self):
        if self.isEmpty():
            return None

        results = self.items()
        st = str(results.__next__())
        for i in results:
            st = st +"->" +str(i)
        return st

    #使用linklist[i]取出第i个值
    def __getitem__(self, item):
        if self.isEmpty():
            return None
        elif (item < 0) | (item >= self.length()):
            raise IndexError
        else:
            prob = self.__head
            cur = 0
            while cur < item:
                prob = prob.nextNode
                cur += 1
            return prob.value

   #使用[]给第i个赋值
    def __setitem__(self, key, value):
        if self.isEmpty():
            return None
        elif (key < 0) | (key >= self.length()):
            raise IndexError
        elif key >0:
            prob = self.__head
            cur = 0
            newNode = Node(value)
            while cur < key:
                pre = prob
                prob = prob.nextNode
                cur += 1
            pre.nextNode = newNode
            newNode.nextNode = prob.nextNode
        else:
            prob = self.__head
            newNode = Node(value)
            newNode.nextNode = prob.nextNode
            self.__head = newNode



if __name__ == '__main__':
    linklist = LinkedList()

    for i in range(5):
        linklist.append(i)
    print(linklist)

    linklist.append(12)
    print(linklist)

    linklist.insert(3, 3.3)
    print(linklist)

    #linklist.insert(34,12)

    linklist.remove(4)
    print(linklist)

    linklist.remove(444)
    print(linklist)

    print(linklist.find(3))

    print(linklist[3])

    linklist[0] = 999
    print(linklist)

    linklist[5] = 555
    print(linklist)





