import stack
#栈的应用
#1.进制转换
def convert(num,base):
    '''将10进制数num转化为base进制数'''
    digit = ['0',"1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    S = stack.Stack()
    while(num > 0):
        value = num % base
        num //= base
        S.push(digit[value])

    while S.size > 0:
        print(S.pop())

#convert(89,2)
print("第一题：")
convert(2013,5)
print("……………………………………")

#2.多括号匹配
def paren(exp):
    dic = {")":"(","}":"{","]":"["}
    S = stack.Stack()
    for value in exp:
        if value in dic.values():
            S.push(value)
        elif S.size == 0:
            return False
        else:
            if dic[value] != S.pop():
                return False
    return S.size == 0
print("第二题：")
#exp = ["(",")","(","(",")",")"]
exp = ["(",")","{","{","[","]"]
print(paren(exp))
print("……………………………………")

#3.栈混洗
#A top:1->2->3:tail
#S push 1,push 2,pop 2,pop 1,push 3
#B top:2->1->3
def shufflestack(innum,outnum):
    '''innum与outnum是list，他们的首元素代表栈顶'''
    S = stack.Stack()
    n = len(innum)
    i = 0
    for j in outnum:
        while j!=S.top():
            S.push(innum[i])
            i+=1
            if i > n-1:
                return False

        if S.size != 0:
            S.pop()
        else:
            return False
    return True
print("第三题：")
#innum = [1,2,3]
#outnum = [2,1,3]
innum = [1,2,3]
outnum = [3,1,2]
print("是否栈混洗：",shufflestack(innum,outnum))
print("……………………………………")






