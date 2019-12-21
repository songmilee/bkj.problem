import sys
import math

def main():
    m = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    list = []

    MIN_VAL = 10001
    resultSum = 0

    for i in range(m, n + 1):
        if(i==0) : continue

        result = calcPerfectSquare(i)

        if(result):
            list.append(i)
            resultSum += i
            MIN_VAL = min(MIN_VAL, i)

    #result print
    if len(list) > 0 :
        print(resultSum)
        print(MIN_VAL)
    else:
        print(-1)

def calcPerfectSquare(num):
    isPerfectSquare = False
    sindex = int(math.sqrt(num))

    for i in range(sindex, num + 1):
        if((i * i) == num):
            isPerfectSquare = True
            break

    return isPerfectSquare

if __name__ == "__main__":
    main()