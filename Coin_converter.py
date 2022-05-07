#!/usr/bin/python3
while True:
    seleccion = input("""¿Qué moneda desea convertir?
        1) Cop a Dolar
        2) Dolar a cop
        3) Salir


        Respuesta: """)

    if (seleccion != '1' and seleccion != '2' and seleccion != '3'):
        print(f"""            *******************************************\n
            Por favor seleccione una opción válida\n
            *******************************************""")

    if (seleccion == '1'):
        Cop = int (input ("¿Cuántos pesos colombianos desea convertir a dolares?:\n"))
        Cop = float(Cop)
        Valor_dolar = 4050
        dolares = Cop / Valor_dolar
        dolares = round(dolares, 2)
        dolares = str(dolares)
        print(f"Tienes ${dolares} dólares.\n\n")
        continue

    elif (seleccion == '2'):
        dolar = input ("¿Cuántos dolares desea convertir a pesos colombianos?:\n")
        dolar = float(dolar)
        Valor_cop = 4050
        pesos = dolar * Valor_cop
        pesos = int(pesos)
        print(f"Tienes Cop {pesos}.\n\n")

    elif (seleccion == '3'):
        exit(1)
