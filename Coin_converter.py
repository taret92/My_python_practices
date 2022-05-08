#!/usr/bin/python3

def conversor_peso_dolar(tipo_moneda, Valor_dolar):
        Pesos = int (input ("¿Cuántos " + tipo_moneda + "desea convertir a dolares?:\n"))
        Pesos = float(Pesos)
        dolares = Pesos / Valor_dolar
        dolares = round(dolares, 2)
        dolares = str(dolares)
        print(f"Tienes ${dolares} dólares.\n\n")

def conversor_dolar_peso(tipo_moneda, Valor_peso):
        dolares = int (input ("¿Cuántos dólares desea convertir a " + tipo_moneda + "?\n"))
        dolares = float(dolares)
        pesos = dolares * Valor_peso
        pesos = int(pesos)
        pesos = str(pesos)
        print (f"Tienes " + pesos + ".\n\n")
while True:
    moneda = int (input("""¿Qué tipo de conversión desea hacer?.
        1) Peso a Dolar
        2) Dolar a peso
        3) Salir
        Respuesta: """))
    if moneda == 1:

            seleccion = int (input("""¿Qué moneda desea convertir?
        1) Peso colombiano a Dolar  2) peso argentino a dolar
        3) peso mexicano a dolar    4) Salir

        Respuesta: """))

            if (seleccion == 1):
                conversor_peso_dolar("pesos colombianos", 4050)

            if (seleccion == 2):
                conversor_peso_dolar("pesos argentino", 116.30)

            elif (seleccion == 3):
                conversor_peso_dolar("pesos mexicanos", 20.18)
            elif (seleccion == 4):
                exit(1)
            else:
                print(f"""            *******************************************\n
            Por favor selecciones una opcion válida\n
                *******************************************""")
            continue
    if moneda == 2:
            seleccion2 = int (input("""¿Qué moneda desea convertir?
        1) Dolar a peso colombiano  2) Dolar a peso argentino
        3) Dolar a peso mexicano    4) Salir

        Respuesta: """))

            if seleccion2 == 1:
                conversor_dolar_peso("pesos colombianos", 4050)

            if (seleccion2 == 2):
                conversor_dolar_peso("pesos argentinos", 116.30)

            if (seleccion2 == 3):
                conversor_dolar_peso("pesos ,mexicanos", 20.18)
            if (seleccion2 == 4):
                exit(1)
            else:
                print(f"""            *******************************************\n
            Por favor selecciones una opcion válida\n
                *******************************************""")
            continue
    if moneda == 3:
        exit(1)
    else:
        print(f"""            *******************************************\n
            Por favor selecciones una opcion válida\n
                *******************************************""")