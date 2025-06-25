while True:
  print("menu de opciones: ")
  print("1. realizar accion 1")
  print("2. realizar accion 2")
  print("3. salir")

  opcion = input("seleciona una opcion (1-3):")

  if opcion == "1":
     print("has selecionado la opcion 1.")
  elif opcion == "2":
     print("has selecionado la opcion 2.")
  elif opcion == "3":
     print("saliendo del programa.")
     break
  else:
     print("opcion no valida.")