import cmath
import math 
import sympy as Sympy

def calcularEa(xr, xrAnterior):
    resultado = (abs(xr-xrAnterior)/xr)*100
    if resultado < 0:
        resultado = resultado*-1
    return resultado


def metodo1(punto,cifras):
    Listado_Resultante = []
    salida = 0
    valorAnterior = 0
    iteracion = 1
    valor = 0
    es = (10**(2-cifras))/2
    ea = 0
    exponente = 2

    #cabezera de tabla
    header = ['Iteracion', 'Valor', 'Ea','Es']
    Listado_Resultante.append(header)

    while salida == 0:
        if iteracion == 1:
            valor = 1

            #Primera iteracion 
            Listado_Resultante.append([iteracion,1,'N/A',es])

            valorAnterior = punto
            iteracion += 1    
        elif iteracion==2:
            
            valor+=punto/cmath.e
            ea = calcularEa(valor,valorAnterior)

            #agremamos las iteraciones 
            Listado_Resultante.append([iteracion,valor,ea,es])

            valorAnterior = valor
            iteracion += 1
        else:
            valor += (-1*(punto**exponente))/exponente*(cmath.e**exponente)
            
            ea = calcularEa(valor,valorAnterior)

            #agremamos las iteraciones 
            Listado_Resultante.append([iteracion,decimal.Decimal(valor),ea,es])

            valorAnterior = valor
            iteracion += 1
            exponente += 1

            if ea <= es:
                salida = 1
            
    return Listado_Resultante

def metodo2(punto,cifras):
    Listado_Resultante = []
    salida = 0
    valorAnterior = 0
    iteracion = 1
    valor = 0
    es = (10**(2-cifras))/2
    ea = 0
    exponente = 2

    #cabezera de tabla
    header = ['Iteracion', 'Valor', 'Ea','Es']
    Listado_Resultante.append(header)

    while salida == 0:
        if iteracion == 1:
            valor = 1

            #Primera iteracion 
            Listado_Resultante.append([iteracion,1,'N/A',es])

            valorAnterior = punto
            iteracion += 1

        else:
            valor += (punto**(2*exponente))/math.factorial(exponente)
            ea = calcularEa(valor,valorAnterior)

            #agremamos las iteraciones 
            Listado_Resultante.append([iteracion,valor,ea,es])

            valorAnterior = valor
            iteracion += 1
            exponente += 2

            if ea <= es:
                salida = 1
            

    return Listado_Resultante

def metodo3(punto,cifras):
    Listado_Resultante = []
    salida = 0
    valorAnterior = 0
    iteracion = 1
    valor = 0
    es = (10**(2-cifras))/2
    ea = 0
    exponente = 3

    #cabezera de tabla
    header = ['Iteracion', 'Valor', 'Ea','Es']
    Listado_Resultante.append(header)

    while salida == 0:
        if iteracion == 1:
            valor = punto

            #Primera iteracion 
            Listado_Resultante.append([iteracion,valor,'N/A',es])

            valorAnterior = punto
            iteracion += 1

        else:
            valor += ((-1**exponente)/math.factorial((2*exponente)+1))*punto**((2*exponente)+1)
            ea = calcularEa(valor,valorAnterior)

            #agremamos las iteraciones 
            Listado_Resultante.append([iteracion,valor,ea,es])

            valorAnterior = valor
            iteracion += 1
            exponente += 2

            if ea <= es:
                salida = 1
            

    return Listado_Resultante

def metodo4(punto,cifras):
    Listado_Resultante = []
    salida = 0
    valorAnterior = 0
    iteracion = 1
    valor = 0
    es = (10**(2-cifras))/2
    ea = 0
    exponente = 2

    #cabezera de tabla
    header = ['Iteracion', 'Valor', 'Ea','Es']
    Listado_Resultante.append(header)

    while salida == 0:
        if iteracion == 1:
            valor = 1

            #Primera iteracion 
            Listado_Resultante.append([iteracion,valor,'N/A',es])

            valorAnterior = punto
            iteracion += 1

        else:
            valor += ((-1**exponente)/math.factorial(2*exponente))*punto**(2*exponente)
            ea = calcularEa(valor,valorAnterior)

            #agremamos las iteraciones 
            Listado_Resultante.append([iteracion,valor,ea,es])

            valorAnterior = valor
            iteracion += 1
            exponente += 2

            if ea <= es:
                salida = 1
            

    return Listado_Resultante

def metodo5(punto,cifras):
    Listado_Resultante = []
    salida = 0
    valorAnterior = 0
    iteracion = 1
    valor = 0
    es = (10**(2-cifras))/2
    ea = 0
    exponente = 1

    #cabezera de tabla
    header = ['Iteracion', 'Valor', 'Ea','Es']
    Listado_Resultante.append(header)

    while salida == 0:
        if iteracion == 1:
            valor = 1

            #Primera iteracion 
            Listado_Resultante.append([iteracion,valor,'N/A',es])

            valorAnterior = punto
            iteracion += 1

        else:
            valor += (punto**exponente)/math.factorial(exponente)
            ea = calcularEa(valor,valorAnterior)

            #agremamos las iteraciones 
            Listado_Resultante.append([iteracion,valor,ea,es])

            valorAnterior = valor
            iteracion += 1
            exponente += 1

            if ea <= es:
                salida = 1
            

    return Listado_Resultante

def metodo6(punto,cifras):
    Listado_Resultante = []
    salida = 0
    valorAnterior = 0
    iteracion = 1
    valor = 0
    es = (10**(2-cifras))/2
    ea = 0
    exponente = 3

    #cabezera de tabla
    header = ['Iteracion', 'Valor', 'Ea','Es']
    Listado_Resultante.append(header)

    while salida == 0:
        if iteracion == 1:
            valor = punto

            #Primera iteracion 
            Listado_Resultante.append([iteracion,valor,'N/A',es])

            valorAnterior = punto
            iteracion += 1

        else:
            valor += (punto**exponente)/math.factorial(exponente)
            ea = calcularEa(valor,valorAnterior)

            #agremamos las iteraciones 
            Listado_Resultante.append([iteracion,valor,ea,es])

            valorAnterior = valor
            iteracion += 1
            exponente += 2

            if ea <= es:
                salida = 1
            

    return Listado_Resultante

def metodo7(punto,cifras):
    Listado_Resultante = []
    salida = 0
    valorAnterior = 0
    iteracion = 1
    valor = 0
    es = (10**(2-cifras))/2
    ea = 0
    exponente = 2

    #cabezera de tabla
    header = ['Iteracion', 'Valor', 'Ea','Es']
    Listado_Resultante.append(header)

    while salida == 0:
        if iteracion == 1:
            valor = 1

            #Primera iteracion 
            Listado_Resultante.append([iteracion,valor,'N/A',es])

            valorAnterior = punto
            iteracion += 1

        else:
            valor += (punto**exponente)/math.factorial(exponente)
            ea = calcularEa(valor,valorAnterior)

            #agremamos las iteraciones 
            Listado_Resultante.append([iteracion,valor,ea,es])

            valorAnterior = valor
            iteracion += 1
            exponente += 2

            if ea <= es:
                salida = 1
            

    return Listado_Resultante

def metodo8(punto,cifras):
    Listado_Resultante = []
    salida = 0
    valorAnterior = 0
    iteracion = 1
    valor = 0
    es = (10**(2-cifras))/2
    ea = 0
    exponente = 3

    #cabezera de tabla
    header = ['Iteracion', 'Valor', 'Ea','Es']
    Listado_Resultante.append(header)

    while salida == 0:
        if iteracion == 1:
            valor = punto

            #Primera iteracion 
            Listado_Resultante.append([iteracion,valor,'N/A',es])

            valorAnterior = punto
            iteracion += 1

        else:
            valor += ((math.factorial(2*exponente))/(2**exponente*math.factorial(exponente))**2)*((punto**(2*exponente)+1)/(2*exponente)+1)
            ea = calcularEa(valor,valorAnterior)
            
            #agremamos las iteraciones 
            Listado_Resultante.append([iteracion,valor,ea,es])

            valorAnterior = valor
            iteracion += 1
            exponente += 2
            
            if ea <= es:
                salida = 1

    return Listado_Resultante

def metodo9(punto,cifras):
    Listado_Resultante = []
    salida = 0
    valorAnterior = 0
    iteracion = 1
    valor = 0
    es = (10**(2-cifras))/2
    ea = 0
    exponente = 2

    #cabezera de tabla
    header = ['Iteracion', 'Valor', 'Ea','Es']
    Listado_Resultante.append(header)

    while salida == 0:
        if iteracion == 1:
            valor = punto

            #Primera iteracion 
            Listado_Resultante.append([iteracion,valor,'N/A',es])

            valorAnterior = punto
            iteracion += 1

        else:
            valor += ((-1**(exponente-1))/exponente)*(punto**exponente)
            ea = calcularEa(valor,valorAnterior)
            
            #agremamos las iteraciones 
            Listado_Resultante.append([iteracion,valor,ea,es])
            valorAnterior = valor
            iteracion += 1
            exponente += 1

            if ea <= es:
                salida = 1
            
    return Listado_Resultante

def metodo10(punto,cifras):
    Listado_Resultante = []
    salida = 0
    valorAnterior = 0
    iteracion = 1
    valor = 0
    es = (10**(2-cifras))/2
    ea = 0
    exponente = 2

    #cabezera de tabla
    header = ['Iteracion', 'Valor', 'Ea','Es']
    Listado_Resultante.append(header)

    while salida == 0:
        if iteracion == 1:
            valor = 1

            #Primera iteracion 
            Listado_Resultante.append([iteracion,valor,'N/A',es])

            valorAnterior = punto
            iteracion += 1

        else:
            valor += ((-1**exponente)*punto**(2*exponente))
            ea = calcularEa(valor,valorAnterior)
            
            #agremamos las iteraciones 
            Listado_Resultante.append([iteracion,valor,ea,es])

            valorAnterior = valor
            iteracion += 1
            exponente += 2

            if ea <= es:
                salida = 1
            
    return Listado_Resultante

def metodo11(punto,cifras):
    Listado_Resultante = []
    salida = 0
    valorAnterior = 0
    iteracion = 1
    valor = 0
    es = (10**(2-cifras))/2
    ea = 0
    exponente = 3

    #cabezera de tabla
    header = ['Iteracion', 'Valor', 'Ea','Es']
    Listado_Resultante.append(header)

    while salida == 0:
        if iteracion == 1:
            valor = punto

            #Primera iteracion 
            Listado_Resultante.append([iteracion,valor,'N/A',es])

            valorAnterior = punto
            iteracion += 1

        else:
            valor += ((-1**exponente)*punto**((2*exponente)+1)/(2*exponente)+1)
            ea = calcularEa(valor,valorAnterior)

            #agremamos las iteraciones 
            Listado_Resultante.append([iteracion,valor,ea,es])

            valorAnterior = valor
            iteracion += 1
            exponente += 2

            if ea <= es:
                salida = 1
            
    return Listado_Resultante

  
