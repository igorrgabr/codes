a, b, c, d = map(int,input().split())
divid = a + c
div = b

if b != d:
    divid = (a*d) + (c*b)
    div = b*d

d = divid
while d >= 2:
    if divid % d == 0 and div % d == 0:
        divid = divid // d
        div = div // d
    d = d - 1

print(divid, div)