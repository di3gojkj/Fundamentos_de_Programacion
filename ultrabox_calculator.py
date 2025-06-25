def calcular_costo_envio():
    print("=== Calculadora de Costos de Envío UltraBox ===")
    
    peso = float(input("Ingrese el peso de la caja en kilogramos: "))
    largo = float(input("Ingrese el largo de la caja en centímetros: "))
    ancho = float(input("Ingrese el ancho de la caja en centímetros: "))
    alto = float(input("Ingrese el alto de la caja en centímetros: "))
    
    cliente_frecuente = input("¿Es cliente frecuente? : ")
    
    volumen = largo * ancho * alto

    if peso > 10 or volumen > 100000:
        precio_base = 15000
    elif peso >= 5 or volumen >= 50000:
        precio_base = 10000
    else:
        precio_base = 5000
   
    if cliente_frecuente == "si":
        descuento = precio_base * 0.33
        costo_total = precio_base - descuento
    else:
        descuento = 0
        costo_total = precio_base

    print("\n=== Resultado ===")
    print(f"Volumen de la caja: {volumen:.2f} cm³")
    print(f"Precio base: ${precio_base}")
    
    if cliente_frecuente:
        print(f"Descuento por cliente frecuente (33%): ${descuento:.2f}")
    
    print(f"Costo total: ${costo_total:.2f}")

if __name__ == "__main__":
    calcular_costo_envio()