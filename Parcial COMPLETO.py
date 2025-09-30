class Usuario:
    def __init__(self):
        self.usuario = None
        self._contraseña = None
        

    def crear_usuario(self):
        print("\t\t Para iniciar,por favor registrese")
        self.usuario = input("\t\t Usuario: ")
        self._contraseña = input("\t\t Escriba su contraseña (Asegurese de encontrarse en un entorno seguro): ")
        return self.usuario 
    




class BiblioU(Usuario):
    def __init__(self):
        self._codigo = None
        self.nombre = None
        self.categoria = None
    def registrar_libro(self,usuario):
        print("\t\t ----Bienvenido A Registrar Libro----")
        check = input("\t\t Por favor ingrese su usuario :")
        while check != usuario:
            print("\t\t Su nombre de usuario es diferente al otorgado")
            check = input("\t\t Por favor ingrese su usuario :")
        nuevo_libro = BiblioU()
        nuevo_libro.nombre = input("\t\t por favor escriba el nombre del libro: ")
        print("\t\t Escriba la categoria de su libro (Recuerde que solo hay 4 categorias)")
        print("\t\t 1.Novela")
        print("\t\t 2.Cuento")
        print("\t\t 3.Cronica")
        print("\t\t 4.Biografia")
        numero = input("\t\t por favor escriba el número de categoria de su libro: ")
        int(numero)
        while (numero != 1 and  numero != 2 and numero != 3 and  numero != 4):
            print("\t\t Categoria Incorrecta")
            numero = input("\t\t por favor escriba el número de categoria de su libro: ")
        if numero == 1:
            print("Se ha guardado en la categoria Novela")
            nuevo_libro.categoria = numero
        elif numero == 2:
            print("Su libro se ha guardado en Cuentos")
            nuevo_libro.categoria = numero
        elif numero == 3:
            print("Su libro pretenece a las crónicas")
            nuevo_libro.categoria = numero
        else:
            print("Su libro es una biografia")
            nuevo_libro.categoria = numero

    def formalizar_registro(self):
        print(f"\t\t Su libro {self.nombre} con código {self._codigo} de categoria {self.categoria} ha sido Registrado")  
        print("\t\t Muchas Gracias por su respuesta")


def menu():
    print("\t\t ---------Menu de Opciones-------")
    print("\t\t | A) Registrar Usuario         |")
    print("\t\t | B) Registrar Libro           |")
    print("\t\t | C) Salir                     |\n")

def proceso():
    print("\t\t Bienvenido a la Biblioteca Universitaria \n")
    
    while True:
        menu()
        elec = input("\t\t Que opción desea: ")
        
        while (elec != 'a' and elec!= 'A') and (elec !='B' and elec != 'b') and (elec !='C' and elec != 'c'):
            print("\t\t| Opción incorrecta,intente de nuevo")
            elec = input("\t\t DQue opción desea: ")
        
        if elec == 'A' or elec == 'a':
            usuario = Usuario()
            usuario.crear_usuario()
        elif elec =='B' or elec == 'b':
                libro_nuevo = BiblioU()
                libro_nuevo.registrar_libro(usuario.usuario)
                libro_nuevo.formalizar_registro()
        elif elec =='C' or elec =='c':
                print("\t\t Saliendo...")
                break 
                break
        
        



def main():
    proceso()

if __name__ == "__main__":
    main()