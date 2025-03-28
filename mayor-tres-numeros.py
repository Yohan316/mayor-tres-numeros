"""
Determina el mayor de tres números ingresados por el teclado
"""

class OrdenadorTresNumeros:
    def __init__(self, numero1, numero2, numero3):
        self.numero1 = numero1
        self.numero2 = numero2
        self.numero3 = numero3
    def intercambiar_valores(self, numero1, numero2):
        temporal = numero1
        numero1 = numero2
        numero2 = temporal
        return numero1, numero2

    def ingresar_numeros(self):
        self.numero1=int(input("Ingresa el primer numero : "))
        self.numero2=int(input("Ingresa el segundo numero: "))
        self.numero3=int(input("Ingresa el tercer numero : "))

    def ordenar_numeros(self):
        if self.numero1>self.numero2:
           self.numero1, self.numero2 = self.intercambiar_valores(self.numero1, self.numero2)

        if self.numero2>self.numero3:
            self.numero2, self.numero3 = self.intercambiar_valores(self.numero2, self.numero3)

        if self.numero1>self.numero2:
           self.numero1, self.numero2 = self.intercambiar_valores(self.numero1, self.numero2)
    def imprimir_numeros(self):
        print(f"numero ordenados: {self.numero1}, {self.numero2}, {self.numero3}")

if __name__=="__main__":
    numero1=5
    numero2=10
    numero3=1
    numeros = OrdenadorTresNumeros(numero1, numero2, numero3)
    print("\nNUmeros desordenados\n")
    numeros.imprimir_numeros()
    print("\nNUmeros ordenados\n")
    numeros.ordenar_numeros()
    numeros.imprimir_numeros()

    numeros.ingresar_numeros()
    print("\nNUmeros ordenados\n")
    numeros.ordenar_numeros()
    numeros.imprimir_numeros()