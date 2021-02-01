#A.栈的接口与实现
import DisorderDoublelinkedlist as ll
class Stack(ll.Doublelinkedlist):
    #像弹夹一样的栈
    #先进后出，后进先出
    #当用向量派生的时候，是尾端push，尾端remove，尾端top，操作都是O(1)。栈顶是尾端
    #这里是用链表派生的，故是首端push，首端remove，首端top，操作都是O(1)。若链表派生与向量派生一样操作，那么操作都是O(n)。栈顶是首段
    def push(self,e):
        '''入栈'''
        self.insertBefore(0,e)

    def pop(self):
        '''出栈'''
        return self.remove(0)

    def top(self):
        '''取顶'''
        return (self)[0]

if __name__ == '__main__':
    Dll = Stack()
    for i in [1, 1, 2, 4, 7, 8, 7]:
        Dll.push(i)
    print(Dll)
    print("top:",Dll.top())
    print("pop:",Dll.pop())
    print("删除后：",Dll)
