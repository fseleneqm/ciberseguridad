from utilidades import comprobar_numero

# Variable contraseña fija:
contrasena = "EstoEsUnaContrasena123"
#contrasena = input("\nIntroduce una contraseña: \n")
#print(contrasena)

def comprobar_longitud(contrasena):
    if len(contrasena) >= 12:
        return True
    else:
        return False

# Comprobaciones con la contraseña fija
print(comprobar_longitud(contrasena))
print(comprobar_numero(contrasena))

# comprobaciones función comprobar_numero con dos cadenas distintas:
print(comprobar_numero("Hola456"))
print(comprobar_numero("byebye"))

def comprobar_mayuscula(contrasena):
    for i in contrasena:
        if i.isupper():
            return "True"
    return False

# comprobaciones función comprobar_mayuscula
print(comprobar_mayuscula(contrasena))
print(comprobar_mayuscula("sinmayusculas"))

# comprobaciones de longitud con cadenas de 10, 11 y 12 caracteres:
print(comprobar_longitud("Hola123456"))
print(comprobar_longitud("Hola1234567"))
print(comprobar_longitud("Hola12345678"))
