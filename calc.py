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
        pass
    def resta(self,a,b):
        """Esta funcion recibe dos numeros y devuelve la resta
        >>> calc.resta(2,2)
        0
        """
        pass
    def mult(self,a,b):
        """Esta funcion recibe dos numeros y devuelve el producto
        """
        pass
    def div(self,a,b):
        """Esta funcion recibe dos numeros y devuelve el cociente
        >>> calc.div(2,2)
        1
        """
        # Para manejar la division entre cero, se una el try/except prevenir un crash
        try:
        	return a/b
        except ZeroDivisionError:
        	print('ERROR: Division entre cero')        
    def es_par(self,a):
        """Esta funcion recibe un numero y devuelve True en caso de que sea par y False en caso de que sea impar
        >>> calc.es_par(2)
        True
        """
        if a%2==0:
            return True
        else:
            return False

# For testing purposes only
#obj = Calc()			# Assignas una variable para la clase
#obj.div(2,0)			# Mandas a llamar la funcion con (.) operator var.class_method()            