colores = ["rojo", "azul", "verde", "amarillo"]

print("---Lista de colores---")
colores.remove("verde") #remueve de la lista el color verde
colores.append("morado") #agrega el color morado a la lista
colores.insert(2, "naranja") #inserta el color naranja en la posicion 2 de la lista
for color in colores:
    print(f"color {color}")