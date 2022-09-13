while True:
    try:
        N = int(input())
        ss = list(map(int,input().split()))
        if max(ss) >= 20:
            print(3)
        elif 10 <= max(ss) < 20:
            print(2)
        else:
            print(1)
    except EOFError:
        break