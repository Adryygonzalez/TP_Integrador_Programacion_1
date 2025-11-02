import csv
from datetime import datetime
import os
import tkinter as tk
from tkinter import filedialog
from c_funciones_colecciones import *

ENCABEZADOS_ESPERADOS = ['nombre', 'poblacion', 'superficie', 'continente']

def abrir_file_dialog(extension='csv')->str:
    # Crear ventana oculta para abrir filedialog
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal
    root.attributes('-topmost', True) # filedialog toma el foco principal
    # Abrir filedialog grafico para seleccionar archivo
    ruta = filedialog.askopenfilename(title=f'Seleccionar archivo {extension.upper()}',filetypes=[(f'Archivos {extension.upper()}', f'*.{extension.lower()}'), ('Todos los archivos', '*.*')])
    root.destroy()
    return ruta

def convertir_lectura_en_paises(lineas:list[str],paises:list[dict])->str:
    errores_conversion = []
    for numero_fila, fila in enumerate(lineas[1:], start=2):
        partes = fila.strip().split(',')
        if len(partes) < len(ENCABEZADOS_ESPERADOS):
            errores_conversion.append(numero_fila)               
            continue  
        nombre = partes[0].strip()
        poblacion_str = partes[1].strip()
        superficie_str = partes[2].strip()
        continente = partes[3].strip()            
        if not nombre or not continente or not poblacion_str.replace('.', '').isdigit() or not superficie_str.replace('.', '').isdigit():
            errores_conversion.append(numero_fila)
            continue            
        pais = crear_pais(nombre, int(poblacion_str), float(superficie_str), continente)
        paises.append(pais)  
    if errores_conversion:
        mensaje = f'Carga parcial, se encontraron {len(errores_conversion)} errores en las filas: {errores_conversion}'
    else:
        mensaje = 'Carga completada con éxito.'
    return mensaje

def cargar_paises(paises:list[dict])->tuple[bool,str,str]:
    '''
    Carga paises desde un archivo CSV seleccionado por el usuario.
    
    La funcion abre un dialogo grafico para que el usuario seleccione un
    archivo CSV. Luego valida que el archivo tenga los encabezados correctos
    y procesa cada fila. Los registros validos se agregan a 'paises',
    mientras que los invalidos se excluyen.
    
    Parametros:
        paises (list[dict]): Lista donde se almacenaran los paises cargados.
        
    Retorna:
        Una tupla[bool,str,str] donde el booleano indica true para exito, el primer str los registros invalidos(si los hubiese) y 
        el segundo la ruta del archivo o false para cualquier fallo, el primer str con el mensaje de error y el segundo str vacio.      
    ''' 
    ruta = abrir_file_dialog()    
    if not ruta:
        return (False,'No se selecciono ningún archivo.','') 
    if not ruta.lower().endswith('.csv'):
        return (False,'El archivo seleccionado no es CSV','')    
    with open(ruta, newline='', encoding='utf-8-sig') as archivo:
        lineas = archivo.readlines()    
        encabezados = lineas[0].strip().split(',')
        if encabezados != ENCABEZADOS_ESPERADOS:
            return (False,f'Encabezados incorrectos. Se esperaban {ENCABEZADOS_ESPERADOS} pero se encontraron {encabezados}','')        
        mensaje = convertir_lectura_en_paises(lineas,paises)
    return (True,mensaje,ruta)

def guardar_paises_en_csv(paises: list[dict[str, object]], ruta: str):
    '''
    Guarda una lista de países en un archivo CSV en la ruta indicada.
    
    Parámetros:
        paises (list[dict]): Lista de diccionarios con los datos de los países.
        ruta (str): Ruta completa o nombre del archivo CSV de salida.
    '''
    lineas = [','.join(ENCABEZADOS_ESPERADOS) + '\n']
    for pais in paises:
        linea = f'{pais['nombre']},{pais['poblacion']},{pais['superficie']},{pais['continente']}\n'
        lineas.append(linea)
    with open(ruta, 'w', encoding='utf-8-sig') as archivo:
        archivo.writelines(lineas)

def generar_nombre_archivo(nombre:str,*,extension='csv')->str:
    '''
    Crea el nombre completo de un archivo con la extension seleccionada.
        
    Parámetros:
        nombre (str): string para el nombre del archivo.
        extension (str, opcional): string para la extencion del archivo. Por defecto CSV.
    Retorno:
        Si el nombre del archivo no existe, retorna el nombre con la extension seleccionada.
        Si el nombre ya existe, retorna el nombre con la hora de creacion y la extension seleccionada.
    '''
    nombre_completo = f'{nombre}.{extension}'    
    if os.path.exists(nombre_completo):
        nombre_completo = f'{nombre}_{datetime.now().strftime("%H_%M_%S")}.{extension}'
    return nombre_completo



