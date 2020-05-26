import sys

def main():
    X = int(sys.stdin.readline())
    origin_val_list = [64]
    total_val = sum(origin_val_list)

    while total_val > X :
        min_val = min(origin_val_list)
        min_val_half = int(min_val / 2)

        total_val = sum(origin_val_list) - min_val + min_val_half

        if total_val >= X:
            origin_val_list.remove(min_val)
            origin_val_list.append(min_val_half)
        else:
            origin_val_list.remove(min_val)
            origin_val_list.append(min_val_half)
            origin_val_list.append(min_val_half)

        total_val = sum(origin_val_list)
    
    print(len(origin_val_list))

if __name__ == "__main__":
    main()