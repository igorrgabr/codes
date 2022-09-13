n1, n2, n3, n4 = map(float,input().split())
media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / 10
if media >= 7.0:
  print("Media: {:.1f}".format(media))
  print("Aluno aprovado.")
elif media < 5.0:
  print("Media: {:.1f}".format(media))
  print("Aluno reprovado.")
elif 5.0 <= media <= 6.9:
  ne = float(input())
  final = (media + ne) / 2
  print("Media: {:.1f}".format(media))
  print("Aluno em exame.")
  print("Nota do exame:",ne)
  if final >= 5.0:
    print("Aluno aprovado.")
  elif final <= 4.9:
    print("Aluno reprovado.")
  print("Media final: {:.1f}".format(final))