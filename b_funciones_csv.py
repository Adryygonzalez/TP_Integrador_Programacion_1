import csv
import tkinter as tk
from tkinter import filedialog
from c_funciones_colecciones import *

ENCABEZADOS_ESPERADOS = ['nombre', 'poblacion', 'superficie', 'continente']
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
    exito = False
    mensaje = ''
    errores_conversion = []
    # Crear ventana oculta para abrir dialogo de archivo
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal
    root.attributes('-topmost', True) # filedialog toma el foco principal
    # Abrir dialogo grafico para seleccionar archivo
    ruta = filedialog.askopenfilename(title='Seleccionar archivo CSV', filetypes=[('Archivos CSV', '*.csv'), ('Todos los archivos', '*.*')])
    root.destroy()   
    
    if not ruta:
        mensaje = 'No se selecciono ningún archivo.'
        return (exito,mensaje,'')    
    
    if not ruta.lower().endswith('.csv'):
        mensaje = 'El archivo seleccionado no es CSV'
        return (exito,mensaje,'')
    
    with open(ruta, newline='', encoding='utf-8-sig') as archivo:
        lector = csv.DictReader(archivo)        
        
        if lector.fieldnames != ENCABEZADOS_ESPERADOS:
            mensaje = f'Encabezados incorrectos. Se esperaban {ENCABEZADOS_ESPERADOS} pero se encontraron {lector.fieldnames}'
            return (exito,mensaje,'')
        
        for numero_fila, fila in enumerate(lector, start=2):
            nombre = fila['nombre'].strip()
            poblacion_str = fila['poblacion'].strip()
            superficie_str = fila['superficie'].strip()
            continente = fila['continente'].strip()
            
            if not nombre or not continente or not poblacion_str.replace('.', '').isdigit() or not superficie_str.replace('.', '').isdigit():
                errores_conversion.append(numero_fila)
                continue
            
            pais = crear_pais(nombre, int(poblacion_str), float(superficie_str), continente)
            paises.append(pais)
    
    exito = True
    if errores_conversion:
        mensaje = f'Carga parcial, se encontraron {len(errores_conversion)} errores en las filas: {errores_conversion}'
    else:
        mensaje = 'Carga completada con éxito.'
    return (exito,mensaje,ruta)

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