def verificar_palindromo():
    print("=== Verificador de Palíndromos ===")
    
    # Solicitar la palabra al usuario
    while True:
        palabra = input("Ingrese una palabra de exactamente 7 letras: ")
        if len(palabra) == 7:
            break
        else:
            print(f"Error: La palabra debe tener exactamente 7 letras. Usted ingresó {len(palabra)} letras.")
    
    # Verificar si es palíndromo
    # Un palíndromo se lee igual de izquierda a derecha que de derecha a izquierda
    palabra_invertida = palabra[::-1]
    
    # Mostrar el resultado
    if palabra == palabra_invertida:
        print(f"'{palabra}' → Sí es palíndromo.")
    else:
        print(f"'{palabra}' → No es palíndromo.")

# Ejecutar el programa
if __name__ == "__main__":
    verificar_palindromo()