# Método de pregunta con respuesta de tipo int.
def ask_int(text: str = ""):

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
def ask_float(text: str = ""):

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


# Método de pregunta con respuesta de tipo bool.
def ask_bool(text: str = ""):

    while True:

        # Guarda la respuesta del usuario
        res = input(f"{text} [Y/N]: ")

        if res.upper() == "Y" or res == "1":

            # Si la respuesta es "Y"
            # o "1" devuelve True.

            return True
        
        elif res.upper() == "N" or res == "0":

            # Si la respuesta es "N"
            # o "0" devuelve False.

            return False
        
        else:
            # Si no es ninguna de las
            # anteriores, el valor
            # no es válido.

            print("The value is not of type bool.")
            print("Try again...")
