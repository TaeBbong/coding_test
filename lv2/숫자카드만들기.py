'''
# 문제
숫자카드 만들기

# 키워드
최대공약수(유클리드 호제법)

# 풀이
각 배열마다 최대공약수를 구하고, 그 최대공약수의 소인수를 모두 구해놓고,
반대편 배열을 나눠봐서 다 안나눠지는 값 중 가장 큰 값을 출력

# 다른 사람 풀이
reduce 함수를 활용하여 배열의 최대공약수 구하는 것을 자동화
왜 최대공약수로만 나눠보고 끝내도 정답일까?
'''

def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)

def dividers(g):
    divides = [g]

    import math
    gs = int(math.sqrt(g))
    for i in range(gs, 1, -1):
        if g % i == 0:
            divides.append(i)

    return divides

def solution(a, b):
    answer = 0

    a = sorted(a)
    b = sorted(b)

    tmp = a[0]
    for e in a[1:]:
        tmp = gcd(e, tmp)
    
    divides = dividers(tmp)

    for d in divides:
        answer = d
        for e in b:
            if e % d == 0:
                answer = 0
                break
        if answer != 0:
            break
    
    tmp = b[0]
    for e in b[1:]:
        tmp = gcd(e, tmp)

    divides = dividers(tmp)

    answer2 = 0
    for d in divides:
        answer2 = d
        for e in a:
            if e % d == 0:
                answer2 = 0
                break
        if answer2 != 0:
            break

    return answer if answer > answer2 else answer2

if __name__ == "__main__":
    a1 = [10, 17]	
    b1 = [5, 20]
    ans1 = 0

    a2 = [10, 20]	
    b2 = [5, 17]	
    ans2 = 10

    a3 = [14, 35, 119]	
    b3 = [18, 30, 102]	
    ans3 = 7

    print(solution(a1, b1), ans1)
    print(solution(a2, b2), ans2)
    print(solution(a3, b3), ans3)