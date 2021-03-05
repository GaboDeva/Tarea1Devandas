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


def test_check_char():

    # CASO POSITIVO
    # Prueba a check_char con todos los caracteres a-z A-Z
    # suma todos los valores devueltos a "err"
    # El assert espera que err sea 0 ya que se asume
    # que todos estos caracteres devuelvan 0.

    err = 0
    for n in range(65, 91):         # Corrido de valores ASCII A-Z
        c = chr(n)
        err = err + check_char(c)

    for n in range(97, 123):        # Corrido de valores ASCII a-z
        c = chr(n)
        err = err + check_char(c)

    assert err == 0


def test_caps_switch():

    # CASO POSITIVO
    # Prueba a caps_switch con todos los caracteres a-z A-Z
    # Compara si el caracter devuelto es el de entrada en minúscula
    # o viceversa y mantiene a "err" en 0 si se cumple.
    # Si esto no se cumple "err" aumenta a un valor diferente de 0
    # El assert espera que err sea 0 indicando que todo se cumplió.

    err = 0
    for n in range(65, 91):         # Corrido de valores ASCII A-Z
        c = chr(n)
        if caps_switch(c) == chr(n).lower():  # Comparación minus-minus.
            err = err + 0
        else:
            err = err + 1

    for n in range(97, 123):        # Corrido de valores ASCII a-z
        c = chr(n)
        if caps_switch(c) == chr(n).upper():  # Comparación MAYUS-MAYUS.
            err = err + 0
        else:
            err = err + 1

    assert err == 0


def test_check_char_b():

    # CASO NEGATIVO
    # introduce más de un caracter válido a check_char() (ERROR 111)
    # asser espera un valor devuelto 0

    assert check_char("iTcR") == 0


def test_check_char_c():

    # CASO NEGATIVO
    # introduce uno o más caracteres invalidos a check_char() (ERROR 110)
    # asser espera un valor devuelto 0

    assert check_char("%1@") == 0


def test_check_char_d():

    # CASO NEGATIVO
    # introduce un parametro que no es STR o CHR a check_char() (ERROR 112)
    # asser espera un valor devuelto 0

    assert check_char(205) == 0
