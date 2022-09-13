x = first = int(input())
y = sec = int(input())
if first > sec:
    first = y
    sec = x
for i in range(first+1,sec):
    if i % 5 == 2 or i % 5 == 3:
        print(i)