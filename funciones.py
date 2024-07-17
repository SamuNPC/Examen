import random
import statistics
def menu(lista):
    while True:
        i=1
        print()
        for item in lista:
            print(i,'.-',item)
            i+=1
        print(i,'.- Salir')
        opc=input('\nIngrese Opción: ')
        if opc.isdigit():
            opc_int=int(opc)
            if opc_int>=1 and opc_int<=i:
                return opc_int
            else:
                print('\nLa opción debe estar entre 1 y ',i)
        else:
            print('Debe Ingresar un Número')

def generar_sueldos(trabajadores):
    sueldos={trabajador:random.randint(300000,2500000) for trabajador in trabajadores}
    print("---------------------------------\nSueldos de asignados:\n---------------------------------")
    for trabajador, sueldo in sueldos.items():
        print(f"{trabajador}: {sueldo}")
    return sueldos

def clasifica_sueldos(sueldos):
    suma=0
    clasificacion={"Menores a 800000":[],"Entre 800000 y 2000000":[],"Superiores a 2000000":[]}
    for trabajador, sueldo in sueldos.items():
        if sueldo<800000:
            clasificacion['Menores a 800000'].append((trabajador,sueldo))
        elif sueldo>=800000 and sueldo<=2000000:
            clasificacion['Entre 800000 y 2000000'].append((trabajador,sueldo))
        elif sueldo>2000000:
            clasificacion['Superiores a 2000000'].append((trabajador,sueldo))
        suma=suma+int(sueldo)
    print('---------------------------------\nClasificacion de sueldos\n---------------------------------')
    for categoria,empleados in clasificacion.items():
        print(f"\n{categoria}    Total: ",len(empleados))
        print()
        print('Nombre empleado      Sueldo')
        for trabajador,sueldo in empleados:
            print(f"{trabajador}        {sueldo}")
    print('Total =',suma)
           

def ver_estadisticas(sueldos):
    sueldo_mas_alto=max(sueldos.values())
    sueldo_mas_bajo=min(sueldos.values())
    promedio_sueldos=statistics.mean(sueldos.values())
    promedio_geo=statistics.geometric_mean(sueldos.values())
    print('---------------------------------\nEstadisticas\n---------------------------------')
    print('Sueldo mas alto: ',sueldo_mas_alto)
    print('Sueldo mas bajo ',sueldo_mas_bajo)
    print('Promedio de sueldos  ',promedio_sueldos)
    print('Media geometrica  ',promedio_geo)

def reporte_sueldos(sueldos):
    print('Nombre empleado      Sueldo Base     Descuento Salud     Descuento AFP   Sueldo liquido\n-----------------------------------------------------------------------------------------')
    for trabajador,sueldo in sueldos.items():
        descuento_salud=(sueldo*0.07)
        descuento_afp=(sueldo*0.12)
        print(f'{trabajador}        {sueldo}            {int(descuento_salud)}            {int(descuento_afp)}        {(sueldo-descuento_afp)-descuento_salud}')


    