#  완전탐색 - 모의고사

#   논리1. 일단 우리는 문제의 갯수를 모른다.
#   논리2. 정답이 하나도 안맞는다면 result 원소가 0이면 answer에 넣지 않는다. 
#   논리3. 문제의 갯수에 따라서 정답이 얼만큼 반복되는지 끊어 줘야한다. 
#   논리4. 이 문제는 완전탐색 즉 컴터의 노가다힘을 믿고 하는 것이기 때문에 바로
#          while for로 조진다 오케이?

def solution(answers):
    supozas = [[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    result = []
    for supoza, i in zip(supozas, range(len(supozas))):
        count = 0 
        length = len(supoza)
        for j in range(len(answers)):
            if answers[j] == supoza[j%length]:
                count += 1
        if count > 0:
            result.append([count,i+1])
    if result:
        result.sort()
        result = [x[1] for x in result]
        return result
    return []
# ___________________________________________________________
def solution(answers):
    supozas = [[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    result = []
    for supoza, i in zip(supozas, range(len(supozas))):
        count = 0 
        length = len(supoza)
        for j in range(len(answers)):
            if answers[j] == supoza[j%length]:
                count += 1
        if count > 0:
            result.append([count,i+1])  
    if result:
        result.sort(reverse = True)
        print(result)
        result_count = [x[0] for x in result]
        max_count = result_count.count(result_count[0])
        return [result[max_count-x-1][1] for x in range(max_count)]
    return []

# 성공 ^^ 왜 갑자기 성공한거지..  