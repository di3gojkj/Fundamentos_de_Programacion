from random import randint

while True:
    num1 = int(input("Ingrese el primer número del rango: "))
    num2 = int(input("Ingrese el segundo número del rango: "))
    if num1 < num2:
        break
    print("El primer número debe ser menor que el segundo. Intente nuevamente.")

numero_secreto = randint(num1, num2)

print(f"\nSe ha generado un número aleatorio entre {num1} y {num2}.")
print("Tienes 3 intentos para adivinarlo.")

for intento in range(1, 4):
    adivinanza = int(input(f"\nIntento {intento}: Ingrese un número: "))
    

    if adivinanza == numero_secreto:
        print(f"¡Felicitaciones! Adivinaste el número en el intento {intento}.")
        break
    
    if intento < 3:
        if adivinanza > numero_secreto:
            print("El número secreto es menor.")
        else:
            print("El número secreto es mayor.")
        
        if intento == 1:
            diferencia1 = (adivinanza - numero_secreto)
        elif intento == 2:
            diferencia2 = (adivinanza - numero_secreto)
            if diferencia2 < diferencia1:
                print("Estás más cerca que en el primer intento.")
            else:
                print("Estás más lejos que en el primer intento.")
    else:
        print(f"¡Perdiste! El número secreto era {numero_secreto}.")
