import funciones
trabajadores=["Juan Perez","Maria Garcia","Carlos Lopez","Ana Martinez","Pedro Rodrigues","Laura Hernandez","Miguel Sanguez","Isabel Gomez","Francisca Dias","Elena Fernandez"]
opciones=["Asignar sueldos aleatorios","Clasificar sueldos","Ver estadisticas","Reporte de sueldos"]
sueldos=None
while True:
    opc=funciones.menu(opciones)
    if opc==1:
        sueldos=funciones.generar_sueldos(trabajadores)
    elif opc==2:
        if sueldos==None:
            print('Debe asignar sueldos para usar esta opcion') 
        else:   
            clasificacion=funciones.clasifica_sueldos(sueldos)
    elif opc==3:
        if sueldos==None:
            print('Debe asignar sueldos para usar esta opcion')
        else:
            funciones.ver_estadisticas(sueldos)
    elif opc==4:
        if sueldos==None:
            print('Debe asignar sueldos para usar esta opcion')
        else:
            funciones.reporte_sueldos(sueldos)
    elif opc==5:
        print('Finalizando programa...\nDesarrollado por Samuel Canchaya\nRUT 21.545.655-2')
        break
