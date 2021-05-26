# 해쉬 위장 1번째 풀이: 런타임 에러 겁나나는 쓰레기 답..

from itertools import combinations
def solution(clothes):
    answer = 0
    dic = {}
    for clothe in clothes:
        # print("clothe =", clothe)
        if clothe[1] in dic:
            dic[clothe[1]] = dic[clothe[1]] + 1
        else:
            dic[clothe[1]] = 1
    values = list(dic.values())
    answer = sum(values)
    # print(dic)
    keys = list(dic.keys()) 
    # print(keys)
    for i in range(len(keys)-1):
        li = list(combinations(keys, i+2))
        print(li)
        mul =1
        li_len = len(li)
        for j in range(li_len):
            for z in range(i+1):
                mul = mul * dic[li[j][z]]
        answer = answer + mul
    return answer

# 실패 요인 값을 너무 다 구하려하지마라 수학적 사고를 할 것
# --------------------------------------------
def solution(clothes):
    answer = 1
    dic = {}
    for val, key in clothes:
        if key in dic.keys():
            dic[key] += 1            
        else:
            dic[key] = 1

    for val in dic.values():
        answer *= val + 1 //옷을 입지 않은 경우 더해줌

    return answer - 1 // 아무것도 안입었을 때를 빼줌



