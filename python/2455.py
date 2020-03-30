'''
0 32
3 13
28 25
39 0
'''

import sys

def main():
    total = 0
    max_person = -1

    for i in range(4):
        out_station, in_station = map(int, sys.stdin.readline().split(" "))
        total = total + in_station - out_station
        max_person = max(total, max_person)
        
    
    print(max_person)

if __name__ == "__main__":
    main()