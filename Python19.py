turistas = {
    "001": ["Diego Rivas", "Brasil", "12-01-2024"],
    "002": ["Renata Valdes", "Mexico", "23-03-2024"],
    "003": ["Brandon Banda", "Africa", "19-09-2023"],
    "004": ["Matias Olavarria", "Argentina", "28-03-2024"],
    "005": ["Emilia Zamora", "Estados Unidos", "10-05-2024"],
    "006": ["Marduck Cea", "Mexico", "08-12-2023"],
    "007": ["Violeta Rivas", "Brasil", "20-06-2024"],
    "008": ["Damian Rivas", "Estados Unidos", "05-07-2023"],
    "009": ["Carola varas", "Estados Unidos", "15-11-2024"],
    "010": ["Diego Marcos", "Brasil", "03-10-2023"],
}

while True:
        print("\nMENU PRINCIPAL")
        print("1.- Turistas por país.")
        print("2.- Turista por mes.")
        print("3.- Eliminar turista.")
        print("4.- Salir.")

        opcion = int(input("Ingrese una opcion: "))

        if opcion == 1:
            pais = input("Ingrese pais a buscar: ")
            resultado = []
            for id_turista, datos in turistas.items():
                if datos[1].lower() == pais.lower():
                    resultado.append(datos[0])
            if resultado:
                  print("[" + ", ".join([f"'{nombre}'" for nombre in resultado]) + "]")
            else:
                 print("No hay turistas de este pais ")

        elif opcion == 2:
                mes = int(input("Ingrese mes a buscar: "))
                if mes < 1 or mes > 12:
                     print("Debe ingresar un valor entre 1 y 12. Inténtelo nuevamente.")
                total_turistas = len(turistas)
                turistas_mes = 0
    
                for datos in turistas.values():
                    fecha = datos[2]
                    mes_fecha = int(fecha.split('-')[1])
                    if mes_fecha == mes:
                     turistas_mes += 1
    
                porcentaje = (turistas_mes / total_turistas) * 100
                print(f"El número de turistas equivale al {porcentaje:.1f} % del total.")
        
        elif opcion == 3:
             nombre = input("Ingrese el nombre del turista a eliminar: ")

             id_encontrado = None

             for id_turista, datos in turistas.items():
                 if datos[0].lower() == nombre.lower():
                     id_encontrado = id_turista
                     break
    
             if id_encontrado:
                 del turistas[id_encontrado]
                 print("Turista eliminado con éxito.")
             else:
                 print("Turista no encontrado. No se pudo eliminar.")
        
        elif opcion == 4:
             print("Programa terminado...")
             break
        
        else:
             print("Opcion no valida, Ingrese una opcion valida de 1 a 4.")
             continue

