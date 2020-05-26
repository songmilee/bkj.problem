import sys

def main():
    e, s, m = [ int(i) for i in sys.stdin.readline().split(' ')]

    cnt_y = 1
    t_e, t_s, t_m = (1, 1, 1)

    while True:
        if t_e == e and t_s == s and t_m == m:
            break

        cnt_y += 1

        t_e += 1
        t_s += 1
        t_m += 1

        if t_e > 15: t_e = 1
        if t_s > 28: t_s = 1
        if t_m > 19: t_m = 1


    print(cnt_y)

if __name__ == "__main__":
    main()