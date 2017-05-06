class Stack:
    def __init__(self):
        self.stack = []
        self.top = -1

    def push(self, data):
        self.stack.append(data)
        self.top += 1
    
    def pop(self):
        temp = self.stack[self.top]
        del self.stack[self.top]
        self.top -= 1
        return temp
    
    def __str__(self):
        count = 0
        string = ""
        for item in self.stack[::-1]:
            string += (str(item) + "  ")
            if count == 0:
                string += "TOP"
            string += "\n"
            count += 1
        return string


def readString(string):
    stack = Stack()
    for c in string:
        decision = decide(c) 
        if decide(c) == False:
            stack.push(int(c))
        else:
            b = stack.pop()
            a = stack.pop()
            val = decision(a,b)
            stack.push(val)
    return stack.pop()

def decide(char):
    def doMult(a,b):
        return a * b
    def doDiv(a,b):
        return a / b
    def doPlus(a,b):
        return a + b
    def doSub(a,b):
        return a - b
    switcher = {
        "+": doPlus,
        "-": doSub,
        "*": doMult,
        "/": doDiv
    }

    return switcher.get(char, False)

print(readString("34+"))
print(readString("34+7*"))
print(readString("777+-842-/*"))
