def funcionPrincipal(funcionSub1, funcionSub2, par1):
    print("primer funcion")
    funcionSub1(1, par1)
    def funcionEjecutar(par):
        print("Dentro de otra funcion")
        funcionSub2(par)
        
    # return funcionEjecutar() esta haria que funcione directamente la funcion sin guardarla en una variable
    return funcionEjecutar
        

def suma(a, b):
    return a + b

def saludo(nombre):
    print(f"Buenos dias {nombre}")

funcion = funcionPrincipal(suma, saludo, 2)
funcion("matias")