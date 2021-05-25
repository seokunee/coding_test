//해시 전화번호 목록

def solution(phone_book):

    phone_book.sort()

    for i in range(len(phone_book)-1):
        a = len(phone_book[i])
        b = len(phone_book[i+1])
        if a <= b:
            if phone_book[i][:a] == phone_book[i+1][:a] :
                return False
        else:
            if phone_book[i][:b] == phone_book[i+1][:b] :
                return False

    return True    
