# Función que comprueba si la cadena tiene algún dígito
def comprobar_numero(contrasena):
    for i in contrasena:
        if i.isdigit():
            return True
    return False

