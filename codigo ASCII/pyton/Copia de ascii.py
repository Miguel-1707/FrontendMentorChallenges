def choose_input_type():
    
    """Pregunta al usuario el tipo de valor que va a ingresar."""
    
    print("Elige el tipo de valor que vas a ingresar:")
    print("1. Decimal")
    print("2. Binario")
    print("3. ASCII")
    choice = input("Ingresa el número correspondiente a tu elección: ")
    return choice

def utf8_to_decimal_with_exceptions(utf8_string):
    
    """Convierte una cadena UTF-8 a sus equivalentes ASCII, decimal y binario, con excepciones para letras con acento predefinidas."""
    
    try:
        # Definir las letras con acento y sus códigos ASCII fijos
        accent_exceptions = {"á": 160, "Á": 181, "é": 130, "É": 144, "í": 161, "Í": 214, "ó": 162, "Ó": 224, "ú": 163, "Ú": 233}
        

        """Aqui se almacenara la convercion"""
        ascii_output = []
        decimal_output = []
        binary_output = []

        """Este buble itera cada caracter, y devuelve el para almacenarlo"""
        for char in utf8_string:
            if char in accent_exceptions:
                """Agrega el valor al array correspondiente"""
                ascii_output.append(accent_exceptions[char]) 
            else:
                ascii_output.append(ord(char))
            decimal_output.append(ord(char))
            binary_output.append(bin(ord(char))[2:])
                
        return ascii_output, decimal_output, binary_output
    except TypeError:
        print("Error: Entrada no válida. Introduce una cadena UTF-8 válida.")
        return None, None, None

def main():
    """
    Función principal para el programa.
    """
    while True:
        choice = choose_input_type()

        if choice not in ['1', '2', '3']:
            print("Opción no válida. Por favor, elige 1, 2 o 3.")
            continue

        value = input("Introduce el valor correspondiente: ")

        if choice == '1':  # Decimal
            try:
                decimal_input = int(value)
                utf8_string = chr(decimal_input)
            except OverflowError:
                print("Error: El valor ingresado es demasiado grande.")
                continue
        elif choice == '2':  # Binario
            decimal_input = int(value, 2)
            utf8_string = chr(decimal_input)
        else:  # ASCII
            utf8_string = value

        ascii_output, decimal_output, binary_output = utf8_to_decimal_with_exceptions(utf8_string)

        if ascii_output is not None and decimal_output is not None and binary_output is not None:
            print("Cadena en ASCII:", ''.join(map(str, ascii_output)))
            print("Cadena en decimal:", decimal_output)
            print("Decimal a binario:", binary_output)

        restart = input("¿Quieres realizar otra conversión? (s/n): ")
        if restart.lower() != 's':
            break

if __name__ == "__main__":
    main()
