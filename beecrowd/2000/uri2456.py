cards = list(map(int,input().split()))

if cards == sorted(cards):
    print("C")
elif cards == sorted(cards)[::-1]:
    print("D")
else:
    print("N")