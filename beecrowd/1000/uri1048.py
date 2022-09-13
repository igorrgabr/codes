salary = float(input())
new = 0
rate = 0
if salary <= 400:
  new = salary + (salary * 0.15)
  rate = 15
elif 400 < salary <= 800:
  new = salary + (salary * 0.12)
  rate = 12
elif 800 < salary <= 1200:
  new = salary + (salary * 0.10)
  rate = 10
elif 1200 < salary <= 2000:
  new = salary + (salary * 0.07)
  rate = 7
elif salary > 2000:
  new = salary + (salary * 0.04)
  rate = 4
print("Novo salario: {:.2f}".format(new))
print("Reajuste ganho: {:.2f}".format(new - salary))
print("Em percentual: {:d} %".format(rate))