#calculadora de porcentaje de ganancia e iva (volmat)



while True:
    valor_neto = int(input("ingrese el valor neto : "))
    valor_iva= 1.19
    porcentaje_ganancia_general = 1.7
    porcentaje_ganancia_cables = 1.3
    valor_total = float(valor_neto * valor_iva) * porcentaje_ganancia_general
    print(f"el valor total es : {valor_total}")
    
    if valor_neto == 0:
        print("no se presentaron mas valores")
        break
    
