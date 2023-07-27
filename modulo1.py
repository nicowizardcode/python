
class Clientes:
    nombre = "Default"
    edad = 0
    producto = "Default"
    precio = 0
    supermercado = "Default"

    def __init__(self, nombre, edad, producto, precio,supermercado):
        self.nombre = nombre
        self.edad = edad
        self.producto = producto
        self.precio = precio
        self.supermercado = supermercado

    def atributos(self):
        print(self.nombre, ":",sep="")
        print("Edad:", self.edad)
        print("Producto:", self.producto)
        print("Precio:", self.precio)
        print("Supermercado:", self.supermercado)

    #def selecprod(self, producto, precio):

    #def updateprod(self, producto, precio):
        #self.precio = self.precio * 1.15

cliente_01 = Clientes("Nico", 89,"Carne", 2000,"Coto")
cliente_01.atributos()
