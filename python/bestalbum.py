from itertools import groupby

def solution(genres, plays):
    answer = []
    
    key_value = [(genres[i], plays[i], i) for i in range(0, len(genres))]
    key_value.sort(key=lambda x: (x[0], -x[1], x[2]))

    group = groupby(key_value, lambda x: x[0])

    sumGroup = [[i,sum(v[1] for v in j)] for i, j in group]  
    sumGroup.sort(key=lambda x:-x[1])

    print(sumGroup)
    
    for g in sumGroup:
        subList = list(filter(lambda x: x[0] == g[0], key_value))[:2]
        print(subList)
        
        answer += [v[2] for v in subList]
    
    return answer


g = ['classic', 'pop','classic', 'classic', 'pop']  
p = [500, 600, 150, 800, 2500]

print(solution(g, p))