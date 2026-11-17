# Variable:
contrasena = "EstoEsUnaContrasena123"
#contrasena = input("\nIntroduce una contraseña: \n")
print(contrasena)

def comprobar_longitud(contrasena):
    if len(contrasena) >= 8:
        return "True"
    else:
        return "False"

def comprobar_mayuscula(contrasena):
    for i in contrasena:
        if i.isupper():
            return "True"
    return False


print(comprobar_longitud(contrasena))
print(comprobar_mayuscula(contrasena))
print(comprobar_mayuscula("sinmayusculas"))