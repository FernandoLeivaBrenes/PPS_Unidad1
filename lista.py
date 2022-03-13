# lista.py : Introduzca un número del 1 al 20 (sin contarlo) y compruebe si existe en la lista [6,14,11,3,2,1,15,19].

__author__ = 'Fernando Leiva Brenes'
__email__ = 'Fernando.leiva.fp@iescampanillas.com'

def estaEnRango(valor, minimo, maximo):
    # Devuelve True o False determinando que valor se encuentra entre el mínimo y el máximo.
    """
    Parameters
        valor (int) - valor entero a comprobar.
        minimo (int) - valor del numero mínimo a ser comprobado
        maximo (int) - valor del numero máximo a ser comprobado
    Returns
        bool - True if fits between values, False if it doesn't
    """
    if valor in range(minimo, maximo):
        return True
    else:
        return False

def estaEnLista(valor, lista):
    # Devuelve True o False determinando si el valor está en la lista.
    """
    Parameters
        valor (int) - valor entero a comprobar.
        lista (list) - valores entre los que buscar
    Returns
        bool - True if its in list, False if it doesn't
    """
    if valor in lista:
        return True
    else:
        return False

if __name__ == '__main__':
    """
    Raises
        SystemExit (No traceback) - ValueError: No es un número
    """
    # Valores constantes para este ejercicio
    valor__minimo = 1
    valor__maximo = 20
    # Lista indicada para este ejercicio
    lista__valores = [6,14,11,3,2,1,15,19]

    # Get user input and adds it to user__input variable.
    # Clean initial and final spaces from user_input
    # Parse to integer
    try:
        user__input = int(input("Introduce un numero entre 1 y 20: ").strip())
    except Exception as err:
        raise SystemExit("ValueError: No es un número")

    # Devuelve una frase acorde al resultado de estaEnlista
    if estaEnRango(user__input, valor__minimo, valor__maximo):
        print(f"Si, el valor {user__input} se encuentra entre 1 y 20")
    else:
        print(f"No, el valor {user__input} no se encuentra entre los valores por defecto.")

    # Devuelve una frase acorde al resultado de estaEnlista
    if estaEnLista(user__input, lista__valores):
        print(f"Si, el valor {user__input} se encuentra en la lista {lista__valores}.")
    else:
        print(f"No, el valor {user__input} no se encuentra entre los valores de la lista.")