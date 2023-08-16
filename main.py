# Método de pregunta con respuesta de tipo int.
def ask_int(text):

    while True:
        try:
            # Intenta convertir el input a int

            return int(input(f"{text}: "))
        
        except ValueError:
            # En caso de tipo de excepción
            # de tipo "ValueError", se le
            # indica al usuario lo sucedido.

            print("The value is not of type int.")
            print("Try again...")
        
        except:
            # En caso de excepción genérica
            # se le indica al usuario lo sucedido.

            print("The value is not valid.")
            print("Try again...")


# Método de pregunta con respuesta de tipo float.
def ask_float(text):

    while True:
        try:
            # Intenta convertir el input a float

            return float(input(f"{text}: "))
        
        except ValueError:
            # En caso de tipo de excepción
            # de tipo "ValueError", se le
            # indica al usuario lo sucedido.

            print("The value is not of type float.")
            print("Try again...")
        
        except:
            # En caso de excepción genérica
            # se le indica al usuario lo sucedido.

            print("The value is not valid.")
            print("Try again...")