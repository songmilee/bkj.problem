import sys

def main():
    n = int(sys.stdin.readline())

    cnt = 0

    for i in range(1, n + 1):
        val = str(i)
        if len(val) < 3 :
            cnt = cnt + 1
        
        else:
            prev_val = -9999

            for j in range(len(val)):
                if j == 0: continue
                
                diff = (int(val[j]) - int(val[j - 1]))

                if prev_val != -9999 and prev_val != diff:
                    break

                prev_val = diff
                if j == len(val) - 1:
                    cnt = cnt + 1


    print(cnt)

if __name__ == "__main__":
    main()