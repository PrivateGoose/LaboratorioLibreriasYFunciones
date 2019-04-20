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