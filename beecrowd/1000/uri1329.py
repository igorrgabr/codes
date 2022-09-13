while True:
    N = int(input())

    if N == 0:
        break

    Ri = map(int,input().split())
    m = 0
    j = 0

    for i in Ri:
        if i == 0:
            m += 1
        elif i == 1:
            j += 1
    
    print(f"Mary won {m} times and John won {j} times")