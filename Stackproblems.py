#implement two stack in an array 
# approch 1: devide the aray into two halves , but it is space inefficient approch
# approch 2: pushing start from both the ends 
class TwoStackArray:
    def __init__(self, maxSize):
        self.max = maxSize
        self.array = [-1 for i in range(self.max)]
        self.top1 = -1
        self.top2 = self.max
    def push1(self,data):
        if (self.top1 < self.max - 1 and (self.top1 + 1 < self.top2)):
            self.top1 += 1
            self.array[self.top1] = data
        else:
            print("Stack1 overflow .....")
    def pop1(self):
        if (self.top1 < 0):
            print("No elements to be popped in stack1")
            return
        pop = self.array[self.top1]
        self.array[self.top1] = -1
        self.top1 -=1
        return pop
    def peekStack1(self):
        return self.array[self.top1] if self.top1 >=0 else None
    def push2(self,data):
        if (self.top2 >= 1 and (self.top2 - 1 > self.top1)):
            self.top2 -= 1
            self.array[self.top2] = data
        else:
            print("Stack2 overflow .....")
    def pop2(self):
        if (self.top2 >= self.max):
            print("No elements to be popped in stack2")
            return
        pop = self.array[self.top2]
        self.array[self.top2] = -1
        self.top2 +=1
        return pop
    def peekStack12(self):
        return self.array[self.top2] if self.top2 < self.max else None
    def display(self):
        print(f"{self.array} \ntop1 -> {self.top1} \ntop2 -> {self.top2}")
"""tsa = TwoStackArray(5)
tsa.push1(5)
tsa.push2(10)
tsa.push2(15)
tsa.push1(11)
tsa.push2(7)
tsa.push2(20)

print("Popped element from stack1 is " + str(tsa.pop1()))
tsa.push2(40)
print("Popped element from stack2 is " + str(tsa.pop2()))
tsa.display()"""

#Problem 2
#Infix to Postfix conversion
#EX: A+B*C+D ==> ABC*+D+
#EX: (A+B)*C + (D-A)  ==> AB+C*DA-+
#EX: ((A+B)-C*(D/E))+F ==> AB+CDE/*-F+
#EX: a+b*(c^d-e)^(f+g*h)-i ==> abcd^e-fgh*+^*+i-

infix = "" #input()
stack = []
def isOperator(x):
    if x in ['+','-','*','/','%','^']:
        return True
    return False
#top 
precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
def notGreater(element,top):
    try:
        if precedence[element]<=precedence[top]:
            return True
    except KeyError:
        return False

for i in range(len(infix)):
    element = infix[i]
    if isOperator(element):
        if len(stack)==0:
            stack.append(element)
        elif stack[-1] == '(':
            stack.append(element)
        else:
            #pop the elements if input is <= the top element
            while(len(stack) >0 and notGreater(element,stack[-1])):
                print(stack[-1],end="")
                stack = stack[:-1]
            stack.append(element)
    elif element == '(':
        stack.append(element)
    elif element == ')':
        while stack[-1]!='(':
            print(stack[-1],end="")
            stack = stack[:-1]
        stack = stack[:-1]
    else:
        print(element,end="")

while len(stack) != 0:
    print(stack[-1],end="")
    stack = stack[:-1]
#Prefix to Infix
#EX: *-A/BC-/AKL ==> ((A-(B/C))*((A/K)-L))
#ex: *+AB-CD ==> ((A+B)*(C-D))
class Stack:
    def __init__(self):
        self.array = []
        self.top = -1
        self.max = 100000
    def isEmpty(self):
        if self.top == -1:
            return True
        return False
    def isFull(self):
        if self.top == self.max-1:
            return True
        return False
    def push(self,data):
        if self.isFull():
            print("Stack overflow")
            return -1
        else:
            self.array.append(data)
            self.top += 1
    def pop(self):
        if self.isEmpty():
            print("Stack underflow")
            return -1
        else:
            element = self.array.pop()
            self.top -= 1
            return element
    def peek(self):
        if self.isEmpty():
            print("Stack underflow")
            return -1
        else:
            peek = self.pop()
            self.push(peek)
            return peek

prefix = ""#input("Input the prefix")
st = Stack()
for i in range(len(prefix)-1,-1,-1):
    x = prefix[i]
    if isOperator(x):
        x1 = st.pop()
        x2 = st.pop()
        #exp : (x1 x x2)
        exp = f"({x1}{x}{x2})"
        st.push(exp)
    else:
        st.push(x)
#print(st.peek())

#Prefix to Postfix
#EX: *+AB-CD ==> AB+CD-*

prefix = "" #input("Input the prefix")
st = Stack()
for i in range(len(prefix)-1,-1,-1):
    x = prefix[i]
    if isOperator(x):
        x1 = st.pop()
        x2 = st.pop()
        #exp : x1 x2 x
        exp = f"{x1}{x2}{x}"
        st.push(exp)
    else:
        st.push(x)
#print("post fix is "+st.peek())

#Problem 4: Balanced parathesis

inputEx = input("Enter your paranthesis Expression: ")
st = Stack()
brackets = {'[':']','(':')','{':'}'}
flag = True
def topValid(element,top):
    return element == brackets[top]
for element in inputEx:
    if element in brackets:
        st.push(element)
    else:
        currentElement = st.peek()
        if currentElement == -1:
            print("Not Balanced")
            flag = False
            break
        if topValid(element,currentElement):
            st.pop()
        else:
            print("Not Balanced")
            flag = False
            break
if flag:
    print("Balanced")

#