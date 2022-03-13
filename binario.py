# binario.py : Introduzca un número binario e imprima por pantalla el número en formato decimal.

__author__ = 'Fernando Leiva Brenes'
__email__ = 'Fernando.leiva.fp@iescampanillas.com'

def esBinario(strbinario) -> bool:
    # Devuelve True o False si la cadena de caracteres (strbinario) que se ha pasado como parámetro contiene una cadena binaria.
    
    """
    Parameters
        strbinario (string) - Entrada cadena de caracteres
    
    Returns
        bool - True: cadena binaria ; False: cualquier otra cosa.
    """
    # Declare a set of '0' and '1'.
    binarySet = {'0', '1'}
    
    # charSet_strbinario (set) - Convert strbinario (string) to a character set.
    charSet_strbinario = set(strbinario)

    """ 
        Check set charSet_strbinario is same as set binarySet
        or set charSet_strbinario contains only '0'
        or set charSet_strbinario contains only '1'
        or, if any condition is false, raise a failure.
    """
    if binarySet == charSet_strbinario or charSet_strbinario == {'0'} or charSet_strbinario == {'1'}:
        return True
    else:
        return False

def convertDecimalToBinary(binaryNumber) -> int:
    # Devuelve el valor decimal al que pertenece el valor binario recibido (binaryNumber).
    """
    Parameters
        binaryNumber (string) - Entrada cadena de caracteres
    
    Returns
        finalDecimalAmount (int) - Devuelve el valor decimal de la cadena binaria.
    """
    # finalDecimalAmount - Decimal amount
    finalDecimalAmount = 0

    # decimalValue - change adding decimal value.
    decimalValue = 1

    # revese iteration
    for binaryNumberByPosition in binaryNumber[::-1]:
        # Checks binaryNumberByPosition, if is = 1, adds the value of a decimalValue variable
        if int(binaryNumberByPosition) == 1:
            finalDecimalAmount += decimalValue
        # Start with 1 and duplicate its value.
        decimalValue *= 2
    # return finalDecimalValue integer
    return int(finalDecimalAmount)
             

if __name__ == '__main__':
    """
    Raises
        ValueError - Valor introducido inválido.
    """
    # Get user input and adds it to user__input variable.
    user__input = input("Introduce un número en binario: ")

    # Clean initial and final spaces from user_input
    user__input = user__input.strip()

    if user__input == '' or esBinario(user__input) == False:
        raise ValueError("Valor introducido inválido.")
    else:
        print(convertDecimalToBinary(user__input))