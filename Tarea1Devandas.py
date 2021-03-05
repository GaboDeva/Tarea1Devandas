def check_char(c):

    # Este método toma el parametro de entrada y determina
    # si se encuentra dentro del rango A-Z a-z devolviendo 0.
    # En caso de no cumplirse, devuelve un codigo de error
    # específico dependiendo del caso.

    if type(c) == str or type(c) == chr:  # Es el parámetro str o chr?
        prohi = 0

        for i in c:     # Revisa todo el parametro entrado
            n = ord(i)  # em busca de caracteres invalidos

            if ((n >= 65) and (n <= 90)) or ((n >= 97) and (n <= 122)):
                prohi = prohi + 0
            else:       # prohi señala la presencia de caracteres invalidos.
                prohi = prohi + 1

        if prohi != 0:  # al menos un caracter invalido
            return 110  # devuelve error 110
        else:
            if len(c) > 1:  # más de un caracter válido.
                return 111  # devuelve error 111
            else:
                return 0  # un solo caracter valido, devuelve 0.
    else:
        return 112  # entrada no es tipo str o chr, devuelve error 112


def caps_switch(c):

    # Procesa el parametro de entrada con check_char()
    # si es válido, lo pasa a mayúscula si está en minúscula
    # y viceversa

    if check_char(c) != 0:  # Procesa el parametro de entrada
        return check_char(c)

    else:  # confirma que es válido.
        n = ord(c)                   # revisa si el parametro de entrada está
        if (n >= 65) and (n <= 90):  # por código ASCII
            return c.lower()         # está en MAYUS, lo devuelve en minus.
        else:
            return c.upper()         # está en minus, lo devuelve en MAYUS.
