intentos = 3
while intentos > 0:
  if input(">>>Escriba la contraseña: ") == "Diego":
    print("Contraseña correcta")
    break
  intentos = intentos - 1
  print(f"Contraseña incorrecta, le quedan {intentos} intentos")
else:
    print("Se han agotado los intentos: (")