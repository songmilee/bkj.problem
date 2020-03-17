'''
13
but
i
wont
hesitate
no
more
no
more
it
cannot
wait
im
yours
'''

import sys

def main():
    n = int(sys.stdin.readline())
    words = []

    while n > 0 :
        val = sys.stdin.readline().strip()
        if val not in words:
            words.append(val)
        n = n - 1

    words.sort()    
    words.sort(key=len)
    
    for word in words:
        print(word)

if __name__ == "__main__":
    main()