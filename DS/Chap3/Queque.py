#队列,像羽毛球桶一样的，先进先出，在队列尾部插入，顶部删除或查询
import DisorderDoublelinkedlist as ll
class Queque(ll.Doublelinkedlist):
    def enqueue(self,e): #O(n)
        self.insertBefore(self.size,e)

    def dequeue(self): #O(1)
        return self.remove(0)

    def front(self):
        return (self)[0]

if __name__ == '__main__':
    Dll = Queque()
    for i in [1, 1, 2, 4, 7, 8, 7]:
        Dll.enqueue(i)

    print("Dll：",Dll)
    print("删除：",Dll.dequeue())
    print("删除后：",Dll)
    print("首元素：",Dll.front())
