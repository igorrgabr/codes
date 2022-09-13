def primo(num,div):
    for d in range(1,num+1):
        if num % d == 0:
            div += 1
    if div == 2:
        return True

N, M = map(int,input().split())
div = 0

while True:
    P1 = N
    P2 = M
    if primo(P1,div):
        if primo(P2,div):
            print(P1 * P2)
            break
        else:
            M = M - 1
    else:
        N = N - 1