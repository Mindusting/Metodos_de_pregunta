# Método de pregunta con respuesta de typo int.
def ask_int(text):
    while True:
        try:
            return int(input(f"{text}: "))
        
        except ValueError:
            print("The value is not of type int.")
            print("Try again...")
        
        except:
            print("The value is not valid.")
            print("Try again...")