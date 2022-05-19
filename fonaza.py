nombre=input("ingrese su nombre:")
suedob=float(input("ingrese su sueldo bruto:"))
afp=int(input("ingrese cuanton le descuentan el afp:"))
afp1=afp/100
org=input("cua es su organizacion, fonasa o isapre:")
porcentaje=int(input(f"ingrerse cuanto le descuentancan en {org}:"))
org1=porcentaje/100
seguroC=int(input("ingrese su porcentade de su seguro:"))
seguro1=seguroC/100
afpd=suedob*afp1
orgd=suedob*org1
segurod=suedob*seguro1
print(nombre,suedob,afp,org,porcentaje,seguroC)
sumd=suedob-(afpd+orgd+segurod)
print("Menu de opciones:")
print("1: calcular el sueldo imponible")
print("2: calcular los descuentos")
print("3: salir")
opc=int(input("ingrese que opcion desea:"))
while opc !=3:
    if opc==1:
        print(sumd)
        print("Menu de opciones:")
        print("1: calcular el sueldo imponible")
        print("2: calcular los descuentos")
        print("3: salir")
        opc = int(input("ingrese que opcion desea:"))
    elif opc==2:
        print(f"su descuento es afp: {afpd}, org:{orgd}, seguro:{segurod}")
        print("Menu de opciones:")
        print("1: calcular el sueldo imponible")
        print("2: calcular los descuentos")
        print("3: salir")
        opc = int(input("ingrese que opcion desea:"))
else:
    print("usted ha salido")