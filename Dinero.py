importe = float(input("Introduzca una cantidad de dinero: "))
tipos = (("billete/s de",500),("billete/s de",200),("billete/s de",100),("billete/s de",50),("billete/s de",20),("billete/s de",10),("billete/s de",5),("moneda/s de",2),("moneda/s de",1),("moneda/s de",0.50),("moneda/s de",0.20),("moneda/s de",0.10),("moneda/s de",0.05),("moneda/s de",0.02),("moneda/s de",0.01))
for tipo in tipos:
    valor = tipo[1]
    descripcion = tipo[0]
    s = lambda valor, text: valor > 1 and text or text
    if importe / valor > 0:
        print((importe // valor), s((importe // valor),descripcion), valor,"€")
        importe = importe % valor