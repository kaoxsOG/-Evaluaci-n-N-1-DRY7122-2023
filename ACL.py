acl_num = input("Ingrese el número de ACL IPv4: ")

if acl_num.isdigit():
    acl_num = int(acl_num)
    if 1 <= acl_num <= 99:
        print("La ACL", acl_num, "es una ACL Estándar.")
    elif 100 <= acl_num <= 199:
        print("La ACL", acl_num, "es una ACL Extendida.")
    else:
            print("El número", acl_num, "no corresponde a una lista de acceso.")
else:
        print("El valor ingresado no es un número de ACL IPv4 válido.")
        
