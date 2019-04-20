"""
Solución del laboratorio
"""
def mes(x):
    a=max(x)
    b=x.index(a)
    if b == 0:
        c="Enero"
    else:
        if b == 1:
            c="Febrero"
        else:
            if b == 2:
                c="Marzo"
            else:
                if b == 3:
                    c="Abril"
                else:
                    if b == 4:
                        c="Mayo"
                    else:
                        if b == 5:
                            c="Junio"
                        else:
                            if b == 6:
                                c="Julio"
                            else:
                                if b == 7:
                                    c="Agosto"
                                else:
                                    if b == 8:
                                        c="Septiembre"
                                    else:
                                        if b == 9:
                                            c="Octubre"
                                        else:
                                            if b == 10:
                                                c="Noviembre"
                                            else:
                                                if b == 11:
                                                    c="Diciembre"
    print(c)

def des_estandar(x):
    import statistics
    a=statistics.stdev(x)
    return float(a)

guajira=[]
def prom_guajira():
    cont_guajira=0
    for cont_guajira in guajira:
        cont_guajira=sum(guajira)
    prom_guajira=cont_guajira/12
    print("El promedio de la guajira es de: {}".format(prom_guajira))

def max_guajira():
    temp_mayor_guajira=max(guajira)
    print("La temperatura mayor fué: {}".format(temp_mayor_guajira))
    return temp_mayor_guajira

santander=[]
def prom_santander():
    cont_santander=0
    for cont_santander in santander:
        cont_santander=sum(santander)
    prom_santander=cont_santander/12
    print("El promedio de santander es de: {}".format(prom_santander))

def max_santander():
    temp_mayor_santander=max(santander)
    print("La temperatura mayor fué: {}".format(temp_mayor_santander))
    return temp_mayor_santander

narino=[]
def prom_narino():
    cont_narino=0
    for cont_narino in narino:
        cont_narino=sum(narino)
    prom_narino=cont_narino/12
    print("El promedio de Nariño fué: {}".format(prom_narino))

def max_narino():
    temp_mayor_narino=max(narino)
    print("La temperatura mayor fué: {}".format(temp_mayor_narino))
    return temp_mayor_narino


print("Bienvenido al ONM! Este programa esta diseñado para \n ver diferentes registros de la temperatura \n de diversas regiones en un año.")
x=int(input("Por favor ingresa alguna de estas opciones: \n 1:Escoger Guajira \n 2:Escoger Santander \n 3: Escoger Nariño \n 4: Todas las regiones \n Ingresa el valor: "))
if x==1:
    i=0
    for i in range (0,12):
        t1=int(input("Ingresa la temperatura: "))
        guajira.append(t1)
    print("Las temperaturas son: {}".format(guajira))
    temp_mes_gua=guajira[0]
    print("La temperatura de enero es: {}".format(temp_mes_gua))
    temp_mes_gua=guajira[1]
    print("La temperatura de Febrero es: {}".format(temp_mes_gua))
    temp_mes_gua=guajira[2]
    print("La temperatura de Marzo es: {}".format(temp_mes_gua))
    temp_mes_gua=guajira[3]
    print("La temperatura de Abril es: {}".format(temp_mes_gua))
    temp_mes_gua=guajira[4]
    print("La temperatura de Mayo es: {}".format(temp_mes_gua))
    temp_mes_gua=guajira[5]
    print("La temperatura de Junio es: {}".format(temp_mes_gua))
    temp_mes_gua=guajira[6]
    print("La temperatura de Julio es: {}".format(temp_mes_gua))
    temp_mes_gua=guajira[7]
    print("La temperatura de Agosto es: {}".format(temp_mes_gua))
    temp_mes_gua=guajira[8]
    print("La temperatura de Septiembre es: {}".format(temp_mes_gua))
    temp_mes_gua=guajira[9]
    print("La temperatura de Octubre es: {}".format(temp_mes_gua))
    temp_mes_gua=guajira[10]
    print("La temperatura de Noviembre es: {}".format(temp_mes_gua))
    temp_mes_gua=guajira[11]
    print("La temperatura de Diciembre es: {}".format(temp_mes_gua))
    prom_guajira()
    max_guajira()
else:
    if x==2:
        i=0
        for i in range (0,12):
            t2=int(input("Ingresa la temperatura: "))
            santander.append(t2)
        print("Las temperaturas son: {}".format(santander))
        temp_mes_sant=santander[0]
        print("La temperatura de Enero es: {}".format(temp_mes_sant))
        temp_mes_sant=santander[1]
        print("La temperatura de Febrero es: {}".format(temp_mes_sant))
        temp_mes_sant=santander[2]
        print("La temperatura de Marzo es: {}".format(temp_mes_sant))
        temp_mes_sant=santander[3]
        print("La temperatura de Abril es: {}".format(temp_mes_sant))
        temp_mes_sant=santander[4]
        print("La temperatura de Mayo es: {}".format(temp_mes_sant))
        temp_mes_sant=santander[5]
        print("La temperatura de Junio es: {}".format(temp_mes_sant))
        temp_mes_sant=santander[6]
        print("La temperatura de Julio es: {}".format(temp_mes_sant))
        temp_mes_sant=santander[7]
        print("La temperatura de Agosto es: {}".format(temp_mes_sant))
        temp_mes_sant=santander[8]
        print("La temperatura de Septiembre es: {}".format(temp_mes_sant))
        temp_mes_sant=santander[9]
        print("La temperatura de Octubre es: {}".format(temp_mes_sant))
        temp_mes_sant=santander[10]
        print("La temperatura de Noviembre es: {}".format(temp_mes_sant))
        temp_mes_sant=santander[11]
        print("La temperatura de Diciembre es: {}".format(temp_mes_sant))

        prom_santander()
        max_santander()
    else:
        if x==3:
            i=0
            for i in range (0,12):
                t3=int(input("Ingresa la temperatura: "))
                narino.append(t3)
            print("Las temperaturas son: {}".format(narino))
            temp_mes_narino=narino[0]
            print("La temperatura de enero es: {}".format(temp_mes_narino))
            temp_mes_narino=narino[1]
            print("La temperatura de Febrero es: {}".format(temp_mes_narino))
            temp_mes_narino=narino[2]
            print("La temperatura de Marzo es: {}".format(temp_mes_narino))
            temp_mes_narino=narino[3]
            print("La temperatura de Abril es: {}".format(temp_mes_narino))
            temp_mes_narino=narino[4]
            print("La temperatura de Mayo es: {}".format(temp_mes_narino))
            temp_mes_narino=narino[5]
            print("La temperatura de Junio es: {}".format(temp_mes_narino))
            temp_mes_narino=narino[6]
            print("La temperatura de Julio es: {}".format(temp_mes_narino))
            temp_mes_narino=narino[7]
            print("La temperatura de Agosto es: {}".format(temp_mes_narino))
            temp_mes_narino=narino[8]
            print("La temperatura de Septiembre es: {}".format(temp_mes_narino))
            temp_mes_narino=narino[9]
            print("La temperatura de Octubre es: {}".format(temp_mes_narino))
            temp_mes_narino=narino[10]
            print("La temperatura de Noviembre es: {}".format(temp_mes_narino))
            temp_mes_narino=narino[11]
            print("La temperatura de Diciembre es: {}".format(temp_mes_narino))
            prom_narino()
            max_narino()
        else:
            if x==4:
                cont_guajira=0
                i=0
                for i in range (0,12):
                    t1=int(input("Ingresa la temperatura: "))
                    cont_guajira=t1+cont_guajira
                    guajira.append(t1)
                print("Las temperaturas son: {}".format(guajira))
                temp_mes_gua=guajira[0]
                print("La temperatura de Enero es: {}".format(temp_mes_gua))
                temp_mes_gua=guajira[1]
                print("La temperatura de Febrero es: {}".format(temp_mes_gua))
                temp_mes_gua=guajira[2]
                print("La temperatura de Marzo es: {}".format(temp_mes_gua))
                temp_mes_gua=guajira[3]
                print("La temperatura de Abril es: {}".format(temp_mes_gua))
                temp_mes_gua=guajira[4]
                print("La temperatura de Mayo es: {}".format(temp_mes_gua))
                temp_mes_gua=guajira[5]
                print("La temperatura de Junio es: {}".format(temp_mes_gua))
                temp_mes_gua=guajira[6]
                print("La temperatura de Julio es: {}".format(temp_mes_gua))
                temp_mes_gua=guajira[7]
                print("La temperatura de Agosto es: {}".format(temp_mes_gua))
                temp_mes_gua=guajira[8]
                print("La temperatura de Septiembre es: {}".format(temp_mes_gua))
                temp_mes_gua=guajira[9]
                print("La temperatura de Octubre es: {}".format(temp_mes_gua))
                temp_mes_gua=guajira[10]
                print("La temperatura de Noviembre es: {}".format(temp_mes_gua))
                temp_mes_gua=guajira[11]
                print("La temperatura de Diciembre es: {}".format(temp_mes_gua))
                prom_guajira()
                max_guajira()
                cont_santander=0
                i=0
                for i in range (0,12):
                    t2=int(input("Ingresa la temperatura: "))
                    cont_santander=cont_santander+t2
                    santander.append(t2)
                print("Las temperaturas son: {}".format(santander))
                temp_mes_sant=santander[0]
                print("La temperatura de Enero es: {}".format(temp_mes_sant))
                temp_mes_sant=santander[1]
                print("La temperatura de Febrero es: {}".format(temp_mes_sant))
                temp_mes_sant=santander[2]
                print("La temperatura de Marzo es: {}".format(temp_mes_sant))
                temp_mes_sant=santander[3]
                print("La temperatura de Abril es: {}".format(temp_mes_sant))
                temp_mes_sant=santander[4]
                print("La temperatura de Mayo es: {}".format(temp_mes_sant))
                temp_mes_sant=santander[5]
                print("La temperatura de Junio es: {}".format(temp_mes_sant))
                temp_mes_sant=santander[6]
                print("La temperatura de Julio es: {}".format(temp_mes_sant))
                temp_mes_sant=santander[7]
                print("La temperatura de Agosto es: {}".format(temp_mes_sant))
                temp_mes_sant=santander[8]
                print("La temperatura de Septiembre es: {}".format(temp_mes_sant))
                temp_mes_sant=santander[9]
                print("La temperatura de Octubre es: {}".format(temp_mes_sant))
                temp_mes_sant=santander[10]
                print("La temperatura de Noviembre es: {}".format(temp_mes_sant))
                temp_mes_sant=santander[11]
                print("La temperatura de Diciembre es: {}".format(temp_mes_sant))
                prom_santander()
                max_santander()
                cont_narino=0
                i=0
                for i in range (0,12):
                    t3=int(input("Ingresa la temperatura: "))
                    cont_narino=cont_narino+t3
                    narino.append(t3)
                print("Las temperaturas son: {}".format(narino))
                temp_mes_narino=narino[0]
                print("La temperatura de Enero es: {}".format(temp_mes_narino))
                temp_mes_narino=narino[1]
                print("La temperatura de Febrero es: {}".format(temp_mes_narino))
                temp_mes_narino=narino[2]
                print("La temperatura de Marzo es: {}".format(temp_mes_narino))
                temp_mes_narino=narino[3]
                print("La temperatura de Abril es: {}".format(temp_mes_narino))
                temp_mes_narino=narino[4]
                print("La temperatura de Mayo es: {}".format(temp_mes_narino))
                temp_mes_narino=narino[5]
                print("La temperatura de Junio es: {}".format(temp_mes_narino))
                temp_mes_narino=narino[6]
                print("La temperatura de Julio es: {}".format(temp_mes_narino))
                temp_mes_narino=narino[7]
                print("La temperatura de Agosto es: {}".format(temp_mes_narino))
                temp_mes_narino=narino[8]
                print("La temperatura de Septiembre es: {}".format(temp_mes_narino))
                temp_mes_narino=narino[9]
                print("La temperatura de Octubre es: {}".format(temp_mes_narino))
                temp_mes_narino=narino[10]
                print("La temperatura de Noviembre es: {}".format(temp_mes_narino))
                temp_mes_narino=narino[11]
                print("La temperatura de Diciembre es: {}".format(temp_mes_narino))
                prom_narino()
                max_narino()
                cont_general=(((cont_guajira)/12)+((cont_santander)/12)+((cont_narino)/12))/3
                print("El promedio del país fue de: {}".format(cont_general))
                max_temps_prom=(max_guajira()+max_santander()+max_narino())/3
                print("El promedio de las temperaturas más calientes del año fueron de: {}".format(max_temps_prom))
                if (max(santander)>max(narino)) and (max(santander)>max(guajira)):
                    print("La temperatura mayor fue en Santander con: ")
                    print(max(santander))
                    print("En el mes de: ")
                    mes(santander)
                else:
                    if(max(santander)>max(guajira)) and (max(santander)>max(narino)):
                        print("La temperatura mayor fue en Santander con: ")
                        print(max(santander))
                        print("En el mes de: ")
                        mes(santander)
                    else:
                        if(max(guajira)>max(santander)) and (max(guajira)>max(narino)):
                            print("La temperatura mayor fue en La Guajira con: ")
                            print(max(guajira))
                            print("En el mes de: ")
                            mes(guajira)
                        else:
                            if (max(guajira)>max(narino))and (max(guajira)>max(santander)):
                                print("La temperatura mayor fue en La Guajira con : ")
                                print(max(guajira))
                                print("En el mes de: ")
                                mes(guajira)
                            else:
                                if (max(narino)>max(santander))and (max(narino)>max(guajira)):
                                    print("La temperatura mayor fue en Nariño con: ")
                                    print(max(narino))
                                    print("En el mes de: ")
                                    mes(narino)
                                else:
                                    if (max(narino)>max(guajira))and (max(narino)>max(santander)):
                                        print("La temperatura mayor fue en Nariño con: ")
                                        print(max(narino))
                                        print("En el mes de: ")
                                        mes(narino)
                print("La desviación estandar de la temperatura en La Guajira fue de:")
                print(des_estandar(guajira))
                print("La desviación estandar de la temperatura en Santander fue de:")
                print(des_estandar(santander))
                print("La desviación estandar de la temperatura en Nariño fue de:")
                print(des_estandar(narino))