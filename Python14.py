colores = ["rojo", "azul", "verde", "amarillo"]
print("---Lista de colores---")

for color in colores:
    if color == "azul" or color == "verde":
        continue
    print(f"color {color}")
