code1,units1,price1 = map(float,input().split(" "))
code2,units2,price2 = map(float,input().split(" "))
amount = (units1 * price1) + (units2 * price2)
print("VALOR A PAGAR: R$ {:.2f}".format(amount))