from statistics import mean
from e_funciones_generales import *
from d_modelo import *

# =====================
# Mostrar informacion
# =====================
def mostrar_lista(lista:list[dict]):
    '''
    Muestra los elementos de una lista en forma enumerada
    Parámetros:
        lista (list): Lista de elementos a mostrar.
    Retorno:
        None
    ''' 
    print()
    for i, elemento in enumerate(lista):
        print(f'{i+1:>3}. {elemento:<50}')

def mostrar_paises(paises:list[dict]):
    '''
    Muestra en formato tabular una lista de países con sus principales datos.
    
    Parámetros:
        paises (list[dict]): Lista de países.
        
    Retorno:
        None
    '''
    print(f'•{'-'*107}•')
    print(f'| {'Nombre':>20} {'|':>21} {'Datos':>23} {'|':>17} {'Continente':>15}{'|':>7}')    
    print(f'•{'-'*107}•')    
    for indice,pais in enumerate(paises):
        print(f'| {indice+1:>3}. {pais['nombre']:<35} | Pob: {pais['poblacion']:>13} | Sup: {pais['superficie']:>13.12g} | {pais['continente']:<20} {'|'}')
    print(f'•{'-'*107}•')   

def mostrar_cantidad_paises_por_continente(*,paises:list[dict], continentes:list[str]):
    '''
    Muestra la cantidad de países agrupados por continente.
    
    Parámetros:
        paises (list[dict]): Lista de países.
        continentes (list[str]): Lista con los nombres de los continentes.
    Retorno:
        None
    '''
    print(f'•{'-'*42}•')
    print(f'| {'Continente':>10} {'|':>15} {'Cant. paises':>5} {'|':>2}')    
    print(f'•{'-'*42}•') 
    for indice,continente in enumerate(continentes,start=1):
        print(f'| {indice:>2}. {continente:<18} {'|':>3} {contar_paises_por_continente(paises=paises,continente=continente):>5}{'|':>10}')
    print(f'•{'-'*42}•')

def mostrar_promedios_por_continente(*,paises:list[dict], continentes:list[str],campo:str):
    '''
    Muestra el promedio de un campo numérico (ejemplo: población, superficie) agrupado por continente.
    
    Parámetros:
        paises (list[dict]): Lista de países.
        continentes (list[str]): Lista con los nombres de los continentes.
        campo (str): Nombre del campo numérico sobre el cual calcular el promedio.
        
    Retorno:
        None
    '''
    print(f'•{'-'*52}•')
    print(f'| {'Continente':>10} {'|':>15} {f'Promedio {campo}':<20} {'|':>4}')    
    print(f'•{'-'*52}•') 
    for indice,continente in enumerate(continentes,start=1):
        print(f'| {indice:>2}. {continente:<18} {'|':>3} {calcular_promedio_por_continente(paises,continente=continente,campo=campo):>15,.0f}{'|':>10}')
    print(f'•{'-'*52}•')

def mostrar_pais_con_un_campo(*,pais:dict,campo:str):
    '''
    Muestra un país y el valor de un campo específico.
    
    Parámetros:
        pais (dict): Diccionario con los datos del país.
        campo (str): Nombre del campo a mostrar.
        
    Retorno:
        None
    '''
    print(f'•{'-'*50}•')
    print(f'| {'Nombre':>10} {'|':>15} {f'{campo}':>14} {'|':>8}')    
    print(f'•{'-'*50}•')     
    print(f'| {' ':>2}. {pais['nombre']:<18} {'|':>3} {pais[campo]:>15,.12g}{'|':>8}')
    print(f'•{'-'*50}•')

# =====================
# Busquedas
# =====================
def buscar_paises_por_nombre(paises:list[dict], nombre:str)->list[dict]:
    '''
    Busca países por coincidencia exacta o parcial en una lista de diccionarios.
        
    Parámetros
    paises (list[dict]): Lista de países representados como diccionarios.
    nombre (str): Nombre (o parte del nombre) del país a buscar.
    
    Retorna
        
    list[dict]
        - Si encuentra una coincidencia exacta, devuelve una lista con un solo diccionario correspondiente a ese país.
        - Si no hay coincidencia exacta, devuelve una lista con todos los países cuyo nombre contenga la cadena buscada.
        - Si no encuentra ninguna coincidencia, devuelve una lista vacía.
    '''    
    encontrados = []    
    for pais in paises:
        if normalizar_cadena(pais['nombre']) == normalizar_cadena(nombre):
            return [pais]            
        elif normalizar_cadena(pais['nombre']).startswith(normalizar_cadena(nombre)):
            encontrados.append(pais)    
    return encontrados

def buscar_mayor_campo(paises:list[dict],*,campo='poblacion')->dict:
    '''
    Busca el país que posee el mayor valor en un campo numérico.
    
    Parámetros:
        paises (list[dict]): Lista de países.
        campo (str): Campo numérico a evaluar (por defecto 'poblacion').
        
    Retorno:        
        El país con el mayor valor en el campo especificado.
    '''
    return max(paises, key=lambda pais: pais[normalizar_cadena(campo)])

def buscar_menor_campo(paises:list[dict],*,campo='poblacion')->dict:
    '''
    Busca el país que posee el menor valor en un campo numérico.
        
    Parámetros:
        paises (list[dict]): Lista de países.
        campo (str): Campo numérico a evaluar (por defecto 'poblacion').
        
    Retorno:
        El país con el menor valor en el campo especificado.
    '''
    return min(paises, key=lambda pais: pais[normalizar_cadena(campo)])

def pedir_opcion_listado(mensaje, listado):
    '''
    Muestra un listado y solicita al usuario que seleccione una opción.
    Parámetros:
        mensaje (str): Texto que se mostrará al usuario al pedir la entrada.
        listado (list): Lista de opciones.
    Retorno:
        int: Opción seleccionada (entero dentro del rango válido).
    '''
    mostrar_lista(listado)
    return pedir_entero(mensaje, minimo=1, maximo=len(listado))

def pedir_un_pais(mensaje:str,paises:list[dict])->dict:
    '''
    Muestra el listado de paises, pide la seleccion de uno por consola y retorna dicho pais.
    
    Parámetros:
        mensaje (str): Texto que se mostrará al usuario al pedir la entrada.
        paises (list[dict]): Lista de países.
        
    Retorno:
        El país seleccionado.
    '''
    mostrar_paises(paises)
    posicion = pedir_entero(mensaje,minimo=1,maximo=len(paises))
    return paises[posicion-1]

# =====================
# ABM
# =====================
def existe_pais_en_lista(paises: list[dict], nombre: str)->bool:
    '''
    Busca dentro de una lista la existencia de un pais, lo hace por el campo nombre.
    No distingue entre mayusculas, minisculas ni acentos.
    Parámetros:
        paises (list[dict]): Lista de países.
        nombre (str): Nombre del pais a buscar.
    
    Retorno:
        True si el pais existe dentro de la lista.
        False si no existe.
    '''
    for pais in paises:
        if normalizar_cadena(pais['nombre']) == normalizar_cadena(nombre):
            return True
    return False

def crear_pais_consola(paises: list[dict],continentes:list[str])->bool:
    '''
    Permite crear un nuevo país desde la consola mediante ingreso manual de datos, no acepta duplicados.
    
    Parámetros:
        paises (list[dict]): Lista de diccionarios que contiene los países.
        continentes (list[str]): Lista con los nombres de los continentes.
        
    Retorna:
        bool: True si el país fue creado y agregado correctamente a la lista.
    '''
    while True:
        nombre = pedir_cadena('Ingrese el nombre del pais: ')
        if existe_pais_en_lista(paises,nombre):
            print(f'\n **ERROR** \'{nombre}\' ya existe, debe ingresar uno nuevo!')
            continue
        break
    poblacion = pedir_entero('Ingrese la cantidad de habitantes: ',minimo=1)
    superficie = pedir_flotante('Ingrese la superficie: ',minimo=1)
    posicion = pedir_opcion_listado('Elija un continente: ',continentes[:-1])
    continente = continentes[posicion-1]
    pais = crear_pais(nombre,poblacion,superficie,continente)
    paises.append(pais)
    return True

def actualizar_pais(pais_actualizado: dict, paises: list[dict]) -> bool:
    '''
    Actualiza la información de un país existente dentro de la lista de países.
        
    Parámetros:
        pais_actualizado (dict): Diccionario con los nuevos datos del país.
        paises (list[dict]): Lista de países.
        
    Retorna:
        True si el país fue encontrado y actualizado correctamente, 
        False si no se encontró ningún país con ese nombre.
    '''
    for i, pais in enumerate(paises):
        if normalizar_cadena(pais['nombre']) == normalizar_cadena(pais_actualizado['nombre']):
            paises[i] = pais_actualizado
        return True  
    return False

def eliminar_pais(pais_a_eliminar: dict, paises: list[dict]) -> bool:
    '''
    Elimina un país de la lista.
    
    Parámetros:
        pais_a_eliminar (dict): Diccionario del país a eliminar.
        paises (list[dict]): Lista de países.
        
    Retorna:
        bool: True si el país fue encontrado y eliminado, False si no se encontró.
    '''   
    for i, pais in enumerate(paises):
        if normalizar_cadena(pais['nombre']) == normalizar_cadena(pais_a_eliminar['nombre']):
            del paises[i]
            return True
    return False

# =====================
# Filtros
# =====================
def filtrar_por_continente(paises: list[dict], *, continente='todos')->list[dict]:
    '''
    Filtra los países según el continente especificado.
    
    Parámetros:
        paises (list[dict]): Lista de países.
        continente (str): Nombre del continente por el cual filtrar('todos' para no aplicar filtro).
        
    Retorno:
        list[dict]: 
            Lista de países pertenecientes al continente solicitado.
    '''
    filtrados = []
    for pais in paises:
        if (normalizar_cadena(pais['continente']) == normalizar_cadena(continente)):
            filtrados.append(pais)
    return filtrados

def filtrar_por_rango(paises:list[dict],*,campo:str ,minimo: int, maximo:int)->list[dict]:
    '''
    Filtra los países cuyos valores en un campo numérico estén dentro de un rango.
    
    Parámetros:
        paises (list[dict]): Lista de países.
        campo (str): Nombre del campo numérico a evaluar.
        minimo (int | float): Valor mínimo aceptado.
        maximo (int | float): Valor máximo aceptado.
        
    Retorno:
        list[dict]
            Lista de países que cumplen con la condición de rango.
    '''
    filtrados = []
    for pais in paises:
        if minimo <= pais[campo] and pais[campo] <= maximo:
            filtrados.append(pais)
    return filtrados  

# =====================
# Ordenamientos
# =====================
def ordenar_paises(paises:list[dict],*, clave='nombre', descendente=False)->list[dict]:
    '''
    Ordena una lista de países en función de un campo dado.
    
    Parámetros:
        paises (list[dict]): Lista de países.
        clave (str): Campo por el cual ordenar (por defecto 'nombre').
        descendente (bool): Si es False (por defecto), ordena ascendente.
                            Si es True, ordena de forma descendente. 
                            
    Retorno:
        list[dict]
            Lista de países ordenada según los criterios indicados.
    '''
    return sorted(paises, key=lambda pais: pais[clave], reverse=descendente)

# =====================
# Estadísticas
# =====================
def contar_paises_por_continente(paises:list[dict],*,continente='todos')->int:
    '''
    Cuenta la cantidad de países pertenecientes a un continente.
    
    Parámetros:
        paises (list[dict]): Lista de países.
        continente (str): Nombre del continente a evaluar('todos' para contar global).
    Retorno:
        int
            Cantidad de países en el continente especificado.
    '''
    contador = 0
    for pais in paises:
        if (normalizar_cadena(pais['continente']) == normalizar_cadena(continente)):
            contador += 1
    return contador

def calcular_promedio_por_continente(paises:list[dict],*,continente='amrica del sur',campo='poblacion')->float:
    '''
    Calcula el promedio de un campo numérico para un continente.
    
    Parámetros:
        paises (list[dict]): Lista de países.
        continente (str): Nombre del continente a evaluar('todos' para global).                       
        campo (str): Campo numérico sobre el cual calcular el promedio(por defecto 'poblacion').
    Retorno:
        float
            Promedio del campo solicitado para el continente especificado.
    '''
    datos = [pais[campo] for pais in paises if pais['continente'].lower() == continente.lower()]
    return  mean(datos) 


