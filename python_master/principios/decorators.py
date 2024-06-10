# def funcionPrincipal(funcionSub1, funcionSub2):
#     print("primer funcion")
#     funcionSub1(1, 2)
#     def subFuncionPrincipal():
#         print("Dentro de otra funcion")
#         funcionSub2()
#     subFuncionPrincipal()
        

# def suma(a, b):
#     return a + b

# def saludo():
#     print("Buenos dias")

# funcionPrincipal(suma, saludo)
def funcionPrincipal(funcionSub1, funcionSub2):
    print("primer funcion")
    funcionSub1(1, 2)
    def funcionEjecutar():
        print("Dentro de otra funcion")
        funcionSub2()
        
    # return funcionEjecutar() esta haria que funcione directamente la funcion sin guardarla en una variable
    return funcionEjecutar
        

def suma(a, b):
    return a + b

def saludo():
    print("Buenos dias")

funcion = funcionPrincipal(suma, saludo)
funcion()
