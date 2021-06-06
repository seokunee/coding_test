# 기능개발
def solution(progresses, speeds):
    answer = []
    times = 0
    count = 0
    while len(progresses) >0:
        if (progresses[0] + times * speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count != 0:
                answer.append(count)
                count = 0 
            times += 1
    answer.append(count)
    return answer

# 이렇게 간단한걸... 난 왜 .. 몇시간을.. 사실 while을
# 돌아가는 횟수를 좀 줄이고 싶었다.