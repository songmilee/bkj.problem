'''
2
5
3 2
1 4
4 1
2 3
5 5
7
3 6
7 3
4 2
1 4
5 7
2 5
6 1
'''

import sys

def main():
    T = int(sys.stdin.readline())

    while(T > 0):
        T = T - 1
        N = int(sys.stdin.readline())

        applicant = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(N)]
        applicant.sort(key=lambda x: x[0])
        
        size = len(applicant)
        cnt = 0
        min_value = 100001
        for i in range(size):            
            if i + 1 > size: break

            if min_value > applicant[i][1]:
                min_value = applicant[i][1]
                cnt = cnt + 1
        print(cnt)
        

if __name__ == "__main__":
    main()