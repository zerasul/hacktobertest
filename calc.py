class Calc:
    """
    clase Calc; permite sumar, restar, multiplicar, dividir y distinguir entre numero pare e impar
    >>> calc = Calc()
    """
    def suma(self,a,b):
        """Esta funcion recibe dos numeros y devuelve la suma
        >>> calc.suma(2,2)
        4
        """
        try:
            resultado = a + b
            return resultado
        except TypeError:
            return False

    def resta(self,a,b):
        """Esta funcion recibe dos numeros y devuelve la resta
        >>> calc.resta(2,2)
        0
        """
        try:
            resultado = a - b
            return resultado
        except TypeError:
            return False
        
    def mult(self,a,b):
        """Esta funcion recibe dos numeros y devuelve el producto
        """
        try:
            resultado = a * b
            return resultado
        except TypeError:
            return False
    
    def div(self,a,b):
        """Esta funcion recibe dos numeros y devuelve el cociente
        >>> calc.div(2,2)
        1
        """     
        try:
            resultado = float(a / b)
            return resultado
        except TypeError:
            return False

    def es_par(self,a):
        """Esta funcion recibe un numero y devuelve True en caso de que sea par y False en caso de que sea impar
        >>> calc.es_par(2)
        True
        """
        if a%2==0:
            return True
        else:
            return False
calculos = Calc()
resultado =calculos.div(2,5)
print(resultado)



