# 가장 큰 수
from itertools import permutations
def solution(numbers):
    num = [str(x) for x in numbers]   
    pers= list(permutations(num, len(numbers)))
    per_str = [''.join(per) for per in pers]
    per_str.sort(reverse = True)
    return per_str[0]
# 이건... 왜 틀렸는지 모르겠는 풀이 내 테스트 케이스는 잘만 통과하는데 ... 

# _____________________________________________________________________
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))
    # 이건 인터넷에서 본건데 엄청 참신한 답이다... 이분 수학 잘하는 듯... 