import heapq

def solution(scovile, k):
    answer = -1
    heapq.heapify(scovile)

    size = len(scovile)
    cnt = 0

    while size != 1:
        if(scovile[0] >= k): break    

        cnt += 1

        min_scovile = heapq.heappop(scovile)
        min_second_scovile = heapq.heappop(scovile) * 2

        update_scovile = min_scovile + min_second_scovile
        heapq.heappush(scovile, update_scovile)
        size = len(scovile)
    
    if scovile[0] >= k:
        answer = cnt


    return answer

if __name__ == "__main__":
    # scovile = [1,2,3,9,10,12]
    scovile = [1, 2, 3, 4]
    # k = 7
    k = 30

    s = solution(scovile, 7)
    print(s)