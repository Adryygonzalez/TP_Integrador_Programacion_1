import unicodedata
from sys import maxsize, float_info

def pedir_cadena(mensaje:str, *, largo=50)->str:
    '''
    Solicita al usuario que ingrese una cadena válida.
    Parámetros:
        mensaje (str): Mensaje que se muestra al pedir la entrada.
        largo (int, opcional): Máximo de caracteres permitidos. Por defecto 50 caracteres.
    Retorno:
        str: Cadena ingresada válida.
    '''
    while True:
        cadena = input(mensaje).strip()
        if not cadena:
            print('**ERROR** Debe ingresar un valor.')
            continue
        if len(cadena) > largo:
            print(f'**ERROR** Los datos ingresados NO deben superar los {largo} caracteres.')
            continue
        break
    return cadena

def pedir_cadena_solo_letras(mensaje:str, *, largo=50)->str:
    '''
    Solicita al usuario que ingrese una cadena válida (solo letras).
    Parámetros:
        mensaje (str): Mensaje que se muestra al pedir la entrada.
        largo (int, opcional): Máximo de caracteres permitidos. Por defecto 50 caracteres.
    Retorno:
        str: Cadena ingresada válida.
    '''
    while True:
        cadena = input(mensaje).strip()
        if not cadena.isalpha() or not cadena:
            print('**ERROR** Los datos ingresados deben ser solo letras.')
            continue
        if len(cadena) > largo:
            print(f'**ERROR** Los datos ingresados NO deben superar los {largo} caracteres.')
            continue
        break
    return cadena

def pedir_entero(mensaje:str, *, minimo=-maxsize-1, maximo=maxsize)->int:
    '''
    Solicita al usuario que ingrese un número entero dentro de un rango.
    Parámetros:
        mensaje (str): Mensaje a mostrar.
        minimo (int, opcional): Valor mínimo permitido. Por defecto es el mínimo negativo de un int.
        maximo (int, opcional): Valor máximo permitido. Por defecto es el máximo positivo de un int.
    Retorno:
        int: Número entero válido ingresado por el usuario.
    '''
    while True:
        negativo = False
        numero = input(mensaje).strip()
        if not numero:
            print('**ERROR** Debe ingresar un valor.')
            continue
        if numero[0] == '-':
            negativo = True
            numero = numero.replace('-','')
        if not numero.isdigit():
            print('**ERROR** Los datos ingresados deben ser solo numericos.')
            continue
        numero = int(numero)
        if negativo:
            numero = numero * -1
        if numero < minimo or numero > maximo:
            print(f'**ERROR** El valor ingresado debe estar entre {minimo} y {maximo}.')
            continue
        break
    return numero

def pedir_flotante(mensaje:str, *, minimo=-float_info.max, maximo=float_info.max, precision=2)->float:
    '''
    Solicita al usuario que ingrese un número flotante válido dentro de un rango específico
    y lo redondea a una cantidad determinada de decimales.
    Parámetros:
        mensaje (str): Texto que se mostrará al usuario al pedir la entrada.
        minimo (float, opcional): Valor mínimo permitido. Por defecto es el mínimo negativo de un float.
        maximo (float, opcional): Valor máximo permitido. Por defecto es el máximo positivo de un float.
        precision (int, opcional): Cantidad de decimales a redondear. Por defecto es 2.
    Retorno:
        float: Número flotante válido ingresado por el usuario, redondeado según precision.
    '''
    while True:
        negativo = False
        numero = input(mensaje).strip()
        if not numero:
            print('**ERROR** Debe ingresar un valor.')
            continue
        if numero[0] == '-':
            negativo = True
            numero = numero.replace('-','')      
        if numero.count('.') > 1 or not numero.replace('.','').isdigit():
            print('**ERROR** Los datos ingresados deben ser solo numericos y contener un solo (.).')
            continue
        numero = round(float(numero), precision)
        if negativo:
            numero = numero * -1
        if numero < round(minimo,precision) or numero > round(maximo,precision):
            print(f'**ERROR** El valor ingresado debe estar entre {round(minimo,precision)} y {round(maximo,precision)}.')
            continue
        break
    return numero

def dibujar_titulo(titulo:str,*,tab=0,char='=',cant=0):
    print(f'\n{'\t'*tab} {char*cant} {titulo.upper()} {char*cant}\n')

def normalizar_cadena(texto: str) -> str:
    '''
    Normaliza una cadena de texto eliminando acentos y convirtiéndola a minúsculas.
    
    Parámetros:
        texto (str): Cadena de texto a normalizar.
            
    Retorna:
        str: La cadena normalizada, en minúsculas y sin acentos.
    '''
    return ''.join(c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn').lower()