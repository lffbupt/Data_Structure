import stack
import re

class Caculator:
    def __init__(self):
        self.__input = re.findall(".",input("请输入表达式："))
        #[栈顶][当前]
        self.pri = {
            "+": {"+": ">", "-": ">", "*": "<", "/": "<", "^": "<", "!": "<", "(": "<", ")": ">", "$": ">"},
            "-": {"+": ">", "-": ">", "*": "<", "/": "<", "^": "<", "!": "<", "(": "<", ")": ">", "$": ">"},
            "*": {"+": ">", "-": ">", "*": ">", "/": ">", "^": "<", "!": "<", "(": "<", ")": ">", "$": ">"},
            "/": {"+": ">", "-": ">", "*": ">", "/": ">", "^": "<", "!": "<", "(": "<", ")": ">", "$": ">"},
            "^": {"+": ">", "-": ">", "*": ">", "/": ">", "^": ">", "!": "<", "(": "<", ")": ">", "$": ">"},
            "!": {"+": ">", "-": ">", "*": ">", "/": ">", "^": ">", "!": ">", "(": " ", ")": ">", "$": ">"},
            "(": {"+": "<", "-": "<", "*": "<", "/": "<", "^": "<", "!": "<", "(": "<", ")": "=", "$": " "},
            ")": {"+": " ", "-": " ", "*": " ", "/": " ", "^": " ", "!": " ", "(": " ", ")": " ", "$": " "},
            "$": {"+": "<", "-": "<", "*": "<", "/": "<", "^": "<", "!": "<", "(": "<", ")": " ", "$": "="}
        }
        self.__input += "$"
        self.num = stack.Stack()#运算数栈
        self.st = stack.Stack()#运算符栈
        self.RPN = []

        self.st.push("$")
        self.i = 0

        number = ''
        while self.st.size != 0:
            if self.__input[self.i] in self.pri:
                self.switch()
                number = ''
            else:
                number = number + self.__input[self.i]
                if self.__input[self.i+1] in self.pri:
                    self.num.push(eval(number))
                    self.RPN.append(eval(number))
                self.i += 1

    def switch(self):
        st = self.pri[self.st.top()][self.__input[self.i]]
        if st == "<":
            self.st.push(self.__input[self.i])
            self.i += 1
        elif st == "=":
            self.st.pop()
            self.i += 1
        elif st == ">":
            op = self.st.pop()
            self.RPN.append(op)
            if op == "!":
                value = self.fac(self.num.pop())
                self.num.push(value)
            elif op != "^":
                num2 = self.num.pop()
                num1 = self.num.pop()
                value = eval("%d%s%d"%(num1,op,num2))
                self.num.push(value)
            else:
                num2 = self.num.pop()
                num1 = self.num.pop()
                value = self.power(num1,num2)
                self.num.push(value)

    def fac(self,n):
        an = 1
        for i in range(n):
            an *= (i+1)
        return an

    def power(self,a,b):
        return a**b

    def run(self):
        print("RPN:",self.RPN)
        return self.num.pop()

a = Caculator().run()
print(a)
#(1+2^3!-4)*(5!-(6-(7-(89-0!)))) = 2013
#0!+123+4*(5*6!+7!/8)/9