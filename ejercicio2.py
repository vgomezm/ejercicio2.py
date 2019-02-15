class Libro():
    def __init__(self, nombre, genero, autor,):
        self.nombre = nombre
        self.genero = genero
        self.autor = autor

    def dame_info(self):
        return 'Book({}, {}, {},{})'.format(self.nombre, self.genero, self.autor)

    def prestamo(self):
        prestamo = print("Tienes un mes para devolver el libro")
        return prestamo

    def devolucion(self):
        dias_maximos=30
        if devolucion>dias:
            print("Tienes que pagar 10 euros")
        else:
            print("No tienes que pagar nada")
