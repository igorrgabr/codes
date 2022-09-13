N = int(input())

for i in range(N):
    num = int(input())
    div = 0
    
    for d in range(1,num+1):
        if num % d == 0:
            div += 1

    if (div == 2):
        print(f"{num} eh primo")
    else:
        print(f"{num} nao eh primo")