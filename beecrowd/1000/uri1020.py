age = int(input())
years = age // 365
months = (age % 365) // 30
days = (age % 365) - (months * 30)
print(years,"ano(s)")
print(months,"mes(es)")
print(days,"dia(s)")