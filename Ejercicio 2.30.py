mes = input("Introduzca un mes del año: ")
dia = input("Introduzca el día de la semana en que comienza dicho mes: ")
while True:
    if mes == "enero" or mes == "febrero" or mes == "marzo" or mes == "abril" or mes == "mayo" or mes == "junio" or mes == "julio" or mes == "agosto" or mes == "septiembre" or mes == "octubre" or mes== "noviembre" or mes == "diciembre":
        print(mes.capitalize())
        break
    else:
        print("Error, introduzca un mes correcto.")
        break
while True:
    if dia == "lunes" and (mes == "enero" or mes == "marzo" or mes == "mayo" or mes == "julio" or mes == "agosto" or mes == "octubre" or mes == "diciembre"):
        print("L\tM\tX\tJ\tV\tS\tD")
        print("1\t2\t3\t4\t5\t6\t7")
        print("8\t9\t10\t11\t12\t13\t14")
        print("15\t16\t17\t18\t19\t20\t21")
        print("22\t23\t24\t25\t26\t27\t28")
        print("29\t30\t31")
        break
    elif dia == "martes" and (mes == "enero" or mes == "marzo" or mes == "mayo" or mes == "julio" or mes == "agosto" or mes == "octubre" or mes == "diciembre"):
        print("L\tM\tX\tJ\tV\tS\tD")
        print(" \t1\t2\t3\t4\t5\t6")
        print("9\t10\t11\t12\t13\t14\t15")
        print("16\t17\t18\t19\t20\t21\t22")
        print("23\t24\t25\t26\t27\t28\t29")
        print("30\t31")
        break
    elif dia == "miercoles" and (mes == "enero" or mes == "marzo" or mes == "mayo" or mes == "julio" or mes == "agosto" or mes == "octubre" or mes == "diciembre"):
        print("L\tM\tX\tJ\tV\tS\tD")
        print(" \t \t1\t2\t3\t4\t5")
        print("6\t7\t8\t9\t10\t11\t12")
        print("13\t14\t15\t16\t17\t18\t19")
        print("20\t21\t22\t23\t24\t25\t26")
        print("27\t\28\t29\t30\t31")
        break
    elif dia == "jueves" and (mes == "enero" or mes == "marzo" or mes == "mayo" or mes == "julio" or mes == "agosto" or mes == "octubre" or mes == "diciembre"):
        print("L\tM\tX\tJ\tV\tS\tD")
        print(" \t \t \t1\t2\t3\t4")
        print("5\t6\t7\t8\t9\t10\t11")
        print("12\t13\t14\t15\t16\t17\t18")
        print("19\t20\t21\t22\t23\t24\t25")
        print("26\t27\t28\t29\t30\t31")
        break
    elif dia == "viernes" and (mes == "enero" or mes == "marzo" or mes == "mayo" or mes == "julio" or mes == "agosto" or mes == "octubre" or mes == "diciembre"):
        print("L\tM\tX\tJ\tV\tS\tD")
        print(" \t \t \t \t1\t2\t3")
        print("4\t5\t6\t7\t8\t9\t10")
        print("11\t12\t13\t14\t15\t16\t17")
        print("18\t19\t20\t21\t22\t23\t24")
        print("25\t26\t27\t28\t29\t30\t31")
        break
    elif dia == "sabado" and (mes == "enero" or mes == "marzo" or mes == "mayo" or mes == "julio" or mes == "agosto" or mes == "octubre" or mes == "diciembre"):
        print("L\tM\tX\tJ\tV\tS\tD")
        print(" \t \t \t \t \t1\t2")
        print("3\t4\t5\t6\t7\t8\t9")
        print("10\t11\t12\t13\t14\t15\t16")
        print("17\t18\t19\t20\t21\t22\t23")
        print("24\t25\t26\t27\t28\t29\t30")
        print("31")
        break
    elif dia == "domingo" and (mes == "enero" or mes == "marzo" or mes == "mayo" or mes == "julio" or mes == "agosto" or mes == "octubre" or mes == "diciembre"):
        print("L\tM\tX\tJ\tV\tS\tD")
        print(" \t \t \t \t \t \t1")
        print("2\t3\t4\t5\t6\t7\t8")
        print("9\t10\t11\t12\t13\t14\t15")
        print("16\t17\t18\t19\t20\t21\t22")
        print("23\t24\t25\t26\t27\t28\t29")
        print("30\t31")
        break
    elif dia == "lunes" and (mes == "abril" or mes == "junio" or mes == "septiembre" or mes == "noviembre"):
        print("L\tM\tX\tJ\tV\tS\tD")
        print("1\t2\t3\t4\t5\t6\t7")
        print("8\t9\t10\t11\t12\t13\t14")
        print("15\t16\t17\t18\t19\t20\t21")
        print("22\t23\t24\t25\t26\t27\t28")
        print("29\t30")
        break
    elif dia == "martes" and (mes == "abril" or mes == "junio" or mes == "septiembre" or mes == "noviembre"):
        print("L\tM\tX\tJ\tV\tS\tD")
        print(" \t1\t2\t3\t4\t5\t6")
        print("9\t10\t11\t12\t13\t14\t15")
        print("16\t17\t18\t19\t20\t21\t22")
        print("23\t24\t25\t26\t27\t28\t29")
        print("30")
        break
    elif dia == "miercoles" and (mes == "abril" or mes == "junio" or mes == "septiembre" or mes == "noviembre"):
        print("L\tM\tX\tJ\tV\tS\tD")
        print(" \t \t1\t2\t3\t4\t5")
        print("6\t7\t8\t9\t10\t11\t12")
        print("13\t14\t15\t16\t17\t18\t19")
        print("20\t21\t22\t23\t24\t25\t26")
        print("27\t\28\t29\t30")
        break
    elif dia == "jueves" and (mes == "abril" or mes == "junio" or mes == "septiembre" or mes == "noviembre"):
        print("L\tM\tX\tJ\tV\tS\tD")
        print(" \t \t \t1\t2\t3\t4")
        print("5\t6\t7\t8\t9\t10\t11")
        print("12\t13\t14\t15\t16\t17\t18")
        print("19\t20\t21\t22\t23\t24\t25")
        print("26\t27\t28\t29\t30")
        break
    elif dia == "viernes" and (mes == "abril" or mes == "junio" or mes == "septiembre" or mes == "noviembre"):
        print("L\tM\tX\tJ\tV\tS\tD")
        print(" \t \t \t \t1\t2\t3")
        print("4\t5\t6\t7\t8\t9\t10")
        print("11\t12\t13\t14\t15\t16\t17")
        print("18\t19\t20\t21\t22\t23\t24")
        print("25\t26\t27\t28\t29\t30")
        break
    elif dia == "sabado" and (mes == "abril" or mes == "junio" or mes == "septiembre" or mes == "noviembre"):
        print("L\tM\tX\tJ\tV\tS\tD")
        print(" \t \t \t \t \t1\t2")
        print("3\t4\t5\t6\t7\t8\t9")
        print("10\t11\t12\t13\t14\t15\t16")
        print("17\t18\t19\t20\t21\t22\t23")
        print("24\t25\t26\t27\t28\t29\t30")
        break
    elif dia == "domingo" and (mes == "abril" or mes == "junio" or mes == "septiembre" or mes == "noviembre"):
        print("L\tM\tX\tJ\tV\tS\tD")
        print(" \t \t \t \t \t \t1")
        print("2\t3\t4\t5\t6\t7\t8")
        print("9\t10\t11\t12\t13\t14\t15")
        print("16\t17\t18\t19\t20\t21\t22")
        print("23\t24\t25\t26\t27\t28\t29")
        print("30")
        break
    elif dia == "lunes" and mes == "febrero":
        print("L\tM\tX\tJ\tV\tS\tD")
        print("1\t2\t3\t4\t5\t6\t7")
        print("8\t9\t10\t11\t12\t13\t14")
        print("15\t16\t17\t18\t19\t20\t21")
        print("22\t23\t24\t25\t26\t27\t28")
        break
    elif dia == "martes" and mes == "febrero":
        print("L\tM\tX\tJ\tV\tS\tD")
        print(" \t1\t2\t3\t4\t5\t6")
        print("9\t10\t11\t12\t13\t14\t15")
        print("16\t17\t18\t19\t20\t21\t22")
        print("23\t24\t25\t26\t27\t28")
        break
    elif dia == "miercoles" and mes == "febrero":
        print("L\tM\tX\tJ\tV\tS\tD")
        print(" \t \t1\t2\t3\t4\t5")
        print("6\t7\t8\t9\t10\t11\t12")
        print("13\t14\t15\t16\t17\t18\t19")
        print("20\t21\t22\t23\t24\t25\t26")
        print("27\t28")
        break
    elif dia == "jueves" and mes == "febrero":
        print("L\tM\tX\tJ\tV\tS\tD")
        print(" \t \t \t1\t2\t3\t4")
        print("5\t6\t7\t8\t9\t10\t11")
        print("12\t13\t14\t15\t16\t17\t18")
        print("19\t20\t21\t22\t23\t24\t25")
        print("26\t27\t28")
        break
    elif dia == "viernes" and mes == "febrero":
        print("L\tM\tX\tJ\tV\tS\tD")
        print(" \t \t \t \t1\t2\t3")
        print("4\t5\t6\t7\t8\t9\t10")
        print("11\t12\t13\t14\t15\t16\t17")
        print("18\t19\t20\t21\t22\t23\t24")
        print("25\t26\t27\t28")
        break
    elif dia == "sabado" and mes == "febrero":
        print("L\tM\tX\tJ\tV\tS\tD")
        print(" \t \t \t \t \t1\t2")
        print("3\t4\t5\t6\t7\t8\t9")
        print("10\t11\t12\t13\t14\t15\t16")
        print("17\t18\t19\t20\t21\t22\t23")
        print("24\t25\t26\t27\t28")
        break
    elif dia == "domingo" and mes == "febrero":
        print("L\tM\tX\tJ\tV\tS\tD")
        print(" \t \t \t \t \t \t1")
        print("2\t3\t4\t5\t6\t7\t8")
        print("9\t10\t11\t12\t13\t14\t15")
        print("16\t17\t18\t19\t20\t21\t22")
        print("23\t24\t25\t26\t27\t28")
        break
    else:
        print("Error, introduzca un día correcto.")
        break