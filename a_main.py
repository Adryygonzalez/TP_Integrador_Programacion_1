from b_funciones_csv import *

ruta = ''
paises = []
filtrados = []
continentes = ['Africa', 'America del norte', 'America del sur','America central', 'Europa', 'Asia', 'Oceania', 'Todos']
menu_principal = ['Cargar archivo .csv', 'Agregar un país','Actualizar un país','Buscar país', 'Filtrar países', 'Ordenar países', 
                'Mostrar estadísticas','Eliminar un país', 'Salir']
menu_filtrado = ['Fitrar por contiente', 'Filtrar rango de poblacion', 'Filtrar por rango de superficie' ]
menu_ordenamiento = ['nombre', 'poblacion', 'superficie']
menu_estadisticas = ['País con mayor y menor población', 'País con mayor y menor superficie', 'Promedio de población', 
                    'Promedio de superficie','Cantidad de países por continente']
opciones_actualizar = ['poblacion','superficie']
denegado_sin_archivo = f'DENEGADO - Debe cargar un archivo para poder operar'
denegado_lista_vacia = f'DENEGADO - Debe existir por lo menos un país'

while True:
    dibujar_titulo('menu principal',tab=1,char='=',cant=7)
    opcion_menu = pedir_opcion_listado('Seleccione una opción: ',menu_principal)
    match opcion_menu:
        case 1:
            dibujar_titulo(menu_principal[opcion_menu-1],char='-', cant=3)
            if not ruta:
                while True:
                    opcion = pedir_opcion_listado('Elija una opcion: ',['Cargar un archivo existente','Crear uno nuevo'])
                    if opcion == 1:
                        exito,mensaje, ruta = cargar_paises(paises)
                        dibujar_titulo(f'{mensaje}',char='*',cant=3)
                        if not exito:
                            continue
                    else:
                        ruta = generar_nombre_archivo('paises',extension='csv')                        
                        dibujar_titulo('Archivo creado con exito',char='*',cant=3)
                    break
            else:
                dibujar_titulo(f'DENEGADO - Ya existe un archivo en uso',char='*',cant=3)
        case 2:
            dibujar_titulo(menu_principal[opcion_menu-1],char='-', cant=3)
            if not ruta:
                dibujar_titulo((denegado_sin_archivo if not ruta else denegado_lista_vacia),char='*',cant=3)
                continue
            if crear_pais_consola(paises,continentes):
                guardar_paises_en_csv(paises,ruta)
                dibujar_titulo('País creado y agregado con exito',char='*',cant=3)
        case 3:
            dibujar_titulo(menu_principal[opcion_menu-1],char='-', cant=3)
            if not paises:
                dibujar_titulo((denegado_sin_archivo if not ruta else denegado_lista_vacia),char='*',cant=3)
                continue                
            pais = pedir_un_pais('Seleccione el país que quiere actualizar: ',paises)
            opcion = pedir_opcion_listado('Elija una opción: ',opciones_actualizar)
            if opcion == 1:
                nuevo_valor = pedir_entero(f'Ingrese el nuevo valor de la {opciones_actualizar[opcion-1]} de {pais['nombre']}: ',minimo=1)
            else:
                nuevo_valor = pedir_flotante(f'Ingrese el nuevo valor de la {opciones_actualizar[opcion-1]} de {pais['nombre']}: ',minimo=1)
            pais[opciones_actualizar[opcion-1]] = nuevo_valor
            if actualizar_pais(pais,paises):
                guardar_paises_en_csv(paises,ruta)
                dibujar_titulo(f'Se actualizo la {opciones_actualizar[opcion-1]} de {pais['nombre']} a {nuevo_valor}',char='*',cant=3)
            else:
                dibujar_titulo(f'No se logro actualizar',char='*',cant=3)
        case 4:
            dibujar_titulo(menu_principal[opcion_menu-1],char='-', cant=3)
            if not paises:
                dibujar_titulo((denegado_sin_archivo if not ruta else denegado_lista_vacia),char='*',cant=3)
                continue
            mostrar_paises(buscar_paises_por_nombre(paises,pedir_cadena('Ingrese el nombre del pais que quiere ver: ')))
        case 5:
            dibujar_titulo(menu_principal[opcion_menu-1],char='-', cant=3)
            if not paises:
                dibujar_titulo((denegado_sin_archivo if not ruta else denegado_lista_vacia),char='*',cant=3)
                continue
            opcion = pedir_opcion_listado('Selecciones una opcion: ',menu_filtrado)
            if opcion == 1:               
                filtrados = filtrar_por_continente(paises,continente=continentes[pedir_opcion_listado('Seleccione el continente: ', continentes)-1])
            else:
                rango_minimo = pedir_entero('Ingrese la cantidad minima: ',minimo=1)
                rango_maximo = pedir_entero('Ingrese la cantidad maxima: ',minimo=2)                
                filtrados = filtrar_por_rango(paises, campo='poblacion' if opcion == 2 else 'superficie',minimo=rango_minimo, maximo=rango_maximo)                
            if filtrados:
                mostrar_paises(filtrados)
            else:
                dibujar_titulo('No se econtraron registros con los critrerios de busqueda',char='*',cant=3)
        case 6:
            dibujar_titulo(menu_principal[opcion_menu-1],char='-', cant=3)
            if not paises:
                dibujar_titulo((denegado_sin_archivo if not ruta else denegado_lista_vacia),char='*',cant=3)
                continue
            print('Ordenar por:',end=' ')
            opcion = pedir_opcion_listado('Seleccione una opcion: ', menu_ordenamiento)
            asc = True if pedir_entero('Seleccione (1-Ascendente 2-Descedendete): ',minimo=1,maximo=2) == 2 else False
            mostrar_paises(ordenar_paises(paises,clave=menu_ordenamiento[opcion-1],descendente=asc))
        case 7:
            dibujar_titulo(menu_principal[opcion_menu-1],char='-', cant=3)
            if not paises:
                dibujar_titulo((denegado_sin_archivo if not ruta else denegado_lista_vacia),char='*',cant=3)
                continue
            match pedir_opcion_listado('Elija que estadistica quiere ver: ',menu_estadisticas):
                case 1:
                    dibujar_titulo('Pais con menor poblacion',char='-',cant=1)  
                    mostrar_pais_con_un_campo(pais=buscar_menor_campo(paises,campo='poblacion'),campo='poblacion')
                    dibujar_titulo('Pais con mayor poblacion',char='-',cant=1)  
                    mostrar_pais_con_un_campo(pais=buscar_mayor_campo(paises,campo='poblacion'),campo='poblacion')
                case 2:
                    dibujar_titulo('Pais con menor superficie',char='-',cant=1)
                    mostrar_pais_con_un_campo(pais=buscar_menor_campo(paises,campo='superficie'),campo='superficie')
                    dibujar_titulo('Pais con mayor superficie',char='-',cant=1)
                    mostrar_pais_con_un_campo(pais=buscar_mayor_campo(paises,campo='superficie'),campo='superficie')
                case 3:
                    dibujar_titulo('Promedio de población',char='-',cant=1)
                    mostrar_promedios_por_continente(paises=paises,continentes=continentes,campo='poblacion')
                case 4:
                    dibujar_titulo('Promedio de superficie',char='-',cant=1)
                    mostrar_promedios_por_continente(paises=paises,continentes=continentes,campo='superficie')
                case 5:
                    dibujar_titulo('Cantidad de países por continente',char='-',cant=1)
                    mostrar_cantidad_paises_por_continente(paises=paises,continentes=continentes)  
        case 8:
            dibujar_titulo(menu_principal[opcion_menu-1],char='-', cant=3)
            if not paises:
                dibujar_titulo((denegado_sin_archivo if not ruta else denegado_lista_vacia),char='*',cant=3)
                continue
            pais = pedir_un_pais('Seleccione el país que quiere eliminar: ',paises)
            if eliminar_pais(pais,paises):
                guardar_paises_en_csv(paises,ruta)
                dibujar_titulo(f'Se elimino \'{pais['nombre']}\' con exito',char='*',cant=3)
            else:
                dibujar_titulo(f'No se logro Eliminar',char='*',cant=3)
        case _:
            opcion = pedir_opcion_listado('Elija una opcion: ',['Salir.','Seguir con el programa.'])
            if opcion == 1:
                dibujar_titulo('Fin del programa',char='-', cant=3)
                break