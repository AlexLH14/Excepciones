def division():
    while True:
        try:
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))
            result = num1 / num2
            print("El resultado de la división es:", result)

        except ValueError:
            print("Error: solo introducir números.")
        except ZeroDivisionError:
            print("Error: No es posible dividir entre cero.")
        else:
            break

division()
