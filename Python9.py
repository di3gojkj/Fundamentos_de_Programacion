nota = float(input("introduzca su nota: "))
if 0 <= nota and nota < 5:
  print("Estas Reporbado")
elif 5 <= nota and nota < 7:
  print("Estas Aprobado")
elif 7 <= nota and nota < 9:
  print("Estas Notable")
elif 9 <= nota and nota <= 10:
  print("Estas Sobresaliente")
else:
  print ("Nota no valida, intente nuevamente")