# Consigna del Ejercicio: Sistema de Gestión de Biblioteca
# Descripción:
# Desarrolla un programa que simule un sistema de gestión de una biblioteca. La idea es que puedas administrar libros y usuarios, permitiendo que los usuarios tomen libros prestados y los devuelvan.

# Requisitos:
# Clases principales:

# Libro: Representa los libros disponibles en la biblioteca.
# Atributos: titulo, autor, anio, disponible (indica si está disponible(True) o prestado(False)).
# Métodos: marcar_prestado(), marcar_devuelto().

# Usuario: Representa a los usuarios de la biblioteca.
# Atributos: nombre, id_usuario, libros_prestados (una lista de libros prestados).
# Métodos: tomar_prestado(libro), devolver_libro(libro).

# Clase Biblioteca:
# Administra los libros y usuarios.
# Atributos: libros (lista de objetos Libro), usuarios (lista de objetos Usuario).
# Métodos:
# agregar_libro(libro): Agrega un libro a la biblioteca.
# agregar_usuario(usuario): Registra un nuevo usuario.
# mostrar_libros_disponibles(): Lista los libros disponibles.
# mostrar_prestamos_usuario(usuario): Muestra los libros que tiene un usuario en préstamo.

# Reglas del Sistema:

# Un usuario puede tomar prestado un máximo de 3 libros al mismo tiempo.
# No se puede prestar un libro que ya esté prestado.
# Cuando un libro es devuelto, debe quedar nuevamente disponible.
# Programa Principal:

# Crea algunos libros y usuarios.
# Permite que los usuarios tomen y devuelvan libros mediante interacciones en consola.
# Muestra en pantalla los libros disponibles y los préstamos de cada usuario.
 

class Libro:
    def __init__(self,titulo,autor,anio,disponible): #constructor de la clase libro (instancia la clase)
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.disponible = disponible

    def marcar_prestado(self):
        self.disponible = False

    def marcar_devuelto(self):
        self.disponible = True

    def __str__(self):
        return f"Titulo: {self.titulo}\nAutor: {self.autor}\nAño: {self.anio}\nDisponibilidad: {self.disponible}"

class Usuario:
    def __init__(self,nombre,id,libros_prestados):
        self.nombre = nombre
        self.id = id
        self.libros_prestados = libros_prestados
        self.cantidad_prestados = len(libros_prestados)

    def tomar_prestado(self,libro):
        if libro.disponible==False:
            print("Este libro ya fue prestado!")
        elif(self.cantidad_prestados<=2):
            libro.marcar_prestado()
            self.libros_prestados.append(libro)
            self.cantidad_prestados+=1
        else:
            print(f"{self.nombre} no puede pedir prestado mas libros hasta que devuelva al menos 1!")

    def devolver_libro(self,libro):
        libro.marcar_devuelto()
        for l in self.libros_prestados:
            if libro == l:
                self.libros_prestados.remove(libro)
        self.cantidad_prestados-=1

    def objName_to_arr(self):
        arr = []
        for libro in self.libros_prestados:
            arr.append(libro.titulo)
        return arr

    def __str__(self):
        otr = self.objName_to_arr()
        return f"Nombre: {self.nombre}\nID: {self.id}\nLibros prestados: {otr}"

class Biblioteca:
    def __init__(self,libros,usuarios):
        self.libros = libros
        self.usuarios = usuarios

    def agregar_libro(self,libro):
        self.libros.append(libro)

    def agregar_usuario(self,usuario):
        self.usuarios.append(usuario)

    def mostrar_libros_disponibles(self):
        for libro in self.libros:
            if self.libro.disponible:
                print(f"{libro}\n")

    def mostrar_prestamos_usuarios(self):
        for user in self.usuarios:
            print(f"{user.libros_prestados}\n")

def main():
    libro1 = Libro("nombre1","autor1","2011",True)
    libro2 = Libro("nombre2","autor2","2012",True)
    libro3 = Libro("nombre3","autor3","2013",True)
    libro4 = Libro("nombre4","autor4","2014",False)
    libro5 = Libro("nombre5","autor5","2015",False)
    libro6 = Libro("nombre6","autor6","2016",False)
    libro7 = Libro("nombre7","autor7","2017",False)
    libro8 = Libro("nombre8","autor8","2018",True)
    usuario1 = Usuario("Juan Perez", 1, [])
    usuario2 = Usuario("Julian Alvarez",2,[libro4,libro5])
    usuario3 = Usuario("Lionel Messi",3,[libro6])
    libros = [libro1,libro2,libro3,libro4,libro5,libro6,libro7]
    usuarios = [usuario1,usuario2]
    bibliotecaPrincipal = Biblioteca(libros,usuarios)

    # print("Libros antes: \n")

    # for libro in bibliotecaPrincipal.libros:
    #     print(f"{libro.__str__()}\n")

    # print("Usuarios antes: \n")

    # for usuario in bibliotecaPrincipal.usuarios:
    #     print(f"{usuario.__str__()}\n")

    # bibliotecaPrincipal.agregar_libro(libro8)
    # bibliotecaPrincipal.agregar_usuario(usuario3)

    # print("Libros despues: \n")

    # for libro in bibliotecaPrincipal.libros:
    #     print(f"{libro.__str__()}\n")

    # print("Usuarios despues: \n")

    # for usuario in bibliotecaPrincipal.usuarios:
    #     print(f"{usuario.__str__()}\n")

    usuario1.tomar_prestado(libro3)     # Se puede tomar prestado
    print(usuario1.cantidad_prestados)  # aumento la cantidad de prestados
    usuario1.tomar_prestado(libro4)     # No puedo tomar prestado un libro que ya fue prestado
    print(libro3.disponible)            # Cambia la disponibilidad al tomar prestado

    print(usuario2.cantidad_prestados)  # 2 tomados prestados inicialmente
    print(usuario2.objName_to_arr())
    usuario2.tomar_prestado(libro1)     # 3 tomados prestados
    print(usuario2.objName_to_arr())
    print(usuario2.cantidad_prestados) 
    usuario2.tomar_prestado(libro2)     # no puede tomar mas prestados
    print(usuario2.cantidad_prestados)
    usuario2.tomar_prestado(libro8)     # no puede tomar mas prestados
    print(usuario2.objName_to_arr())
    print(libro5.disponible) 
    usuario2.devolver_libro(libro5)  
    print(usuario2.objName_to_arr())
    print(libro5.disponible)
    print(usuario2.cantidad_prestados)
main()



