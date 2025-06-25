def empresa():
    while True:
        try:
            registro_empleados=int(input("ingrese la cantidad de empleados a registar: "))
            break
        except ValueError:
            print("Error: se debe ingresar un numero entero, intente nuevamente.")
    
    
    mas_de_10 = 0
    menos_de_10 = 0
    
    for _ in range(registro_empleados):
        nombre = input("ingrese nombre del empleado: ")
        x = False
        while not x:
            try:
                antiguedad = int(input("Ingrese los años de antiguedad: "))
                break
                x = True
            except ValueError:
                print("Error: se debe ingresar un numero entero, intente nuevamente.")
                
        if antiguedad > 10:
                mas_de_10 += 1
                print(f"{nombre} tiene más de 10 años de antigüedad")
        elif antiguedad == 10:
                menos_de_10 += 1
                print(f"{nombre} tiene exactamente 10 años de antigüedad")
        else:
                menos_de_10 += 1
                print(f"{nombre} tiene menos de 10 años de antigüedad")
            
    print(f"Se registraron {mas_de_10} empleados con más de 10 años de antigüedad")
    print(f"Se registraron {menos_de_10} empleados con 10 o menos años de antigüedad")
           
empresa()