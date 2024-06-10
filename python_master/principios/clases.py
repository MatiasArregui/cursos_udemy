class Moneda:
    def __init__(self, valor, color, procer):
        self._valor = valor
        self._color = color
        self._procer = procer
        
    @property
    def valor(self):
        return self._valor
    
    @valor.setter
    def valor(self, parametro):
        self._valor = parametro
        
    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, parametro):
        self._color = parametro

    @property
    def procer(self):
        return self._procer
    
    @procer.setter
    def procer(self, parametro):
        self._procer = parametro
    

class Peso(Moneda):
    def __init__(self, valor, color, procer, pais):
        super().__init__(valor, color, procer)
        self._pais = pais
    

moneda1 = Moneda(25, "rojo", "san martin")
print(moneda1.valor)
peso1 = Peso(25, "blanco", "Manuel belgrano", "Argentina")
print(peso1.valor)