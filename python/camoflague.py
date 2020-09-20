# https://www.welcomekakao.com/learn/courses/30/lessons/42578?language=python3
# 확률 !!

def solution(clothes):
    answer = 0

    item_list = dict()

    classifyItems(item_list, clothes)        
    answer = calculateCombiSum(item_list)

    return answer

def classifyItems(item_list, clothes):
    for i in clothes:
        if i[1] in item_list:
            item_list[i[1]] += 1            
        else:
            item_list[i[1]] = 1

def calculateCombiSum(item_list):
    answer = 1
    key_list = item_list.keys()    
    
    for i in key_list:
        answer *= (item_list[i] + 1)
    
    return answer - 1


if __name__ == "__main__":
    clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
    # clothes = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
    s = solution(clothes)

    print(s)