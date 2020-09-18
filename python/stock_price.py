# https://www.welcomekakao.com/learn/courses/30/lessons/42584

def solution(prices):
    size = len(prices)
    answer = [0] * size

    for i in range(0, size):
        for j in range(i + 1, size):
            answer[i] = answer[i] + 1
            if prices[i] > prices[j]: break
    
    return answer

if __name__ == "__main__":
    result = solution([1, 2, 3, 2, 3])
    print(result)