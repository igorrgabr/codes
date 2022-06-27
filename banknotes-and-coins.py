N = float(input())+0.00001
x = N // 100
y = N % 100
print("NOTAS:")
print(int(x),"nota(s) de R$ 100.00")
print(int(y//50),"nota(s) de R$ 50.00")
print(int(y%50//20),"nota(s) de R$ 20.00")
print(int(y%50%20//10),"nota(s) de R$ 10.00")
print(int(y%50%20%10//5),"nota(s) de R$ 5.00")
print(int(y%50%20%10%5//2),"nota(s) de R$ 2.00")
print("MOEDAS:")
print(int(y%50%20%10%5%2//1),"moeda(s) de R$ 1.00")
print(int(y%50%20%10%5%2%1//0.5),"moeda(s) de R$ 0.50")
print(int(y%50%20%10%5%2%1%0.5//0.25),"moeda(s) de R$ 0.25")
print(int(y%50%20%10%5%2%1%0.5%0.25//0.1),"moeda(s) de R$ 0.10")
print(int(y%50%20%10%5%2%1%0.5%0.25%0.1//0.05),"moeda(s) de R$ 0.05")
print(int(y%50%20%10%5%2%1%0.5%0.25%0.1%0.05//0.01),"moeda(s) de R$ 0.01")