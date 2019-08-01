import sys
from collections import deque

n = int(sys.stdin.readline())
que = deque()
while n >= 1 :
    command = sys.stdin.readline()

    if "push_back" in command:
        x = int(command.split(' ')[1])
        que.append(x)
    elif "push_front" in command:
        x = int(command.split(' ')[1])
        que.appendleft(x)
    elif "pop_front" in command:
        val = -1
        if len(que) > 0:
            val = que.popleft()

        print(val)
    elif "pop_back" in command:
        val = -1
        if len(que) > 0:
            val = que.pop()

        print(val)
    elif "size" in command:
        print(len(que))
    elif "empty" in command:
        val = 1

        if len(que) > 0:
            val = 0
        print(val)

    elif "front" in command:
        val = -1

        if len(que) > 0:
            val = que[0]
        print(val)
    elif "back" in command:
        val = -1

        size = len(que)
        if size > 0 :
            val = que[size-1]

        print(val)

    n -= 1