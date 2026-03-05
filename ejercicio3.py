def validar_contrasena(password):
    if len(password) < 10: # Verificar longitud
        return False
    
    if ' ' in password: # Verificar que no contenga espacios
        return False
    
    if not any(c.isupper() for c in password): # Verificar al menos una mayúscula
        return False
    
    if not any(c.isdigit() for c in password): # Verificar al menos un número
        return False
    
    return True

print(validar_contrasena("Abcdef1234")) # Cumple con todos los requisitos
print(validar_contrasena("abcdef1234")) # No tiene mayúscula
print(validar_contrasena("ABCDEFGHIJ")) # No tiene número
print(validar_contrasena("Abcdefg 123")) # Tiene espacio
print(validar_contrasena("Abc123")) # Muy corta