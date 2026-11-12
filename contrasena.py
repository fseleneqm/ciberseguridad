# Variable:
#contrasena = "EstoEsUnaContrasena123"
contrasena = input("\nIntroduce una contraseña: \n")
print(contrasena)

def comprobar_longitud(contrasena):
    if len(contrasena) >= 8:
        return "True"
    else:
        return "False"

print(comprobar_longitud(contrasena))