# Recuerda que cada archivo python es un modulo en si y el grupo de estos se llama "packete"
def suma(*args):
    total = args[0]
    if len(args) > 1:
        for x in args[1:]:
            total+= x
        return total
    else:
        return total

def resta(*args):
    resta = args[0]
    if len(args) > 1:
        for x in args[1:]:
            resta-=x
        return resta
    else:
        return resta

def promedio(*args):
    total = 0
    cont = len(args)
    for x in args:
        total +=x
    return total/cont

def division(parametro1, parametro2):
    division = parametro1 / parametro2
    return division

def multiplicacion(parametro1, parametro2):
    multiplicacion = parametro1 * parametro2
    return multiplicacion

