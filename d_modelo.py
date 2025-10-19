def crear_pais(nombre:str, poblacion:int, superficie:float, continente:str)->dict:
    '''
    Crea un diccionario que representa un país.
    '''
    return {
        'nombre': nombre,
        'poblacion': poblacion,
        'superficie': superficie,
        'continente': continente
    }
