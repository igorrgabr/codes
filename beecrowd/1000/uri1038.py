x,y = map(int,input().split())
price = 0.0
total = 0.0
if x == 1:
    price = 4.0
elif x == 2:
    price = 4.5
elif x == 3:
    price = 5.0
elif x == 4:
    price = 2.0
elif x == 5:
    price = 1.5
total = y * price
print("Total: R$ {:.2f}".format(total))