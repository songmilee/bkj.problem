import sys

class Stack:
    def __init__(self):
        self.stack = []

    def getSize(self):
        return len(self.stack)

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        val = -1

        if self.getSize() > 0:
            val = self.stack.pop()

        return val

    def isEmpty(self):
        val = 1

        if self.getSize() > 0 :
            val = 0

        return val

    def top(self):
        val = -1

        if self.getSize() > 0:
            last_index = self.getSize() - 1
            val = self.stack[last_index]

        return val

def main():
    testCase = int(sys.stdin.readline())
    stack = Stack()

    while testCase > 0:
        command = sys.stdin.readline()

        if "push" in command:
            x = int(command.split(' ')[1])
            stack.push(x)
        elif "top" in command:
            x = stack.top()
            print(x)
        elif "size" in command:
            x = stack.getSize()
            print(x)
        elif "pop" in command:
            x = stack.pop()
            print(x)
        elif "empty" in command:
            x = stack.isEmpty()
            print(x)

        testCase = testCase - 1

if __name__ == "__main__":
    main()