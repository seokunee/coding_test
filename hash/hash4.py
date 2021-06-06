# 베스트 앨범
def solution(genres, plays):
    answer = []
    dic = {}
    add = []
    tc = {}
    for gen, play, vv in zip(genres, plays, range(len(genres)) ):
        if gen in dic.keys():
            dic[gen].append([play,vv])
            tc[gen] += play
        else:
            dic[gen] = [[play,vv]]
            tc[gen] = play
    tc = sorted(tc.items(), key=lambda x: x[1], reverse=True)
    for gen in tc:
        dic[gen[0]].sort(reverse=True)
        answer.append(dic[gen[0]][0][1])
        answer.append(dic[gen[0]][1][1])
    return answer
# 역시나 런타임 에러가 나버렸다....
# ---------------------------------------------

def solution(genres, plays):
    answer = []
    dic = {}
    for i in range(len(genres)):
        if genres[i] in dic:
            dic[genres[i]][0] += plays[i]
            dic[genres[i]][1].append([plays[i],i])
        else:
            dic[genres[i]] = [plays[i], [[plays[i],i]]]
    dic_li = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    for info in dic_li:
        li = sorted(info[1][1], reverse=True)
        answer.append(li[0][1])
        answer.append(li[1][1])
    return answer
#  이것도 런타임 에러남.. 뭐가 문제지...
#  문제는 바로 문제를 잘 안읽었기 때문이야!! 룰이 다 안들어갔잖아..
# __________________________________________________________
def solution(genres, plays):
    answer = []
    dic = {}
    for i in range(len(genres)):
        if genres[i] in dic:
            dic[genres[i]][0] += plays[i]
            dic[genres[i]][1].append([plays[i],i])
        else:
            dic[genres[i]] = [plays[i], [[plays[i],i]]]
    dic_li = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    for info in dic_li:
        print(info)
        li = sorted(info[1][1], key=lambda x: (x[0],-x[1]), reverse=True)
        answer.append(li[0][1])        
        if len(li) > 1:
            answer.append(li[1][1])
    return answer
#  뺌 완벽해...  이를 통해서 lambda 사용법을 배웠다. 
