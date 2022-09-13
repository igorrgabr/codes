salary = float(input())
taxes = 0
if 2000 < salary <= 3000:
  taxes = (salary - 2000) * 0.08
  print("R$ {:.2f}".format(taxes))
elif 3000 < salary <= 4500:
  taxes = (salary - 3000) * 0.18 + (1000 * 0.08)
  print("R$ {:.2f}".format(taxes))
elif salary > 4500:
  taxes = (salary - 4500) * 0.28 + (1500 * 0.18) + (1000 * 0.08)
  print("R$ {:.2f}".format(taxes))
else:
  print("Isento")