class Usuario:
    def __init__(self):
        self.usuario = None
        self._contraseña = None
        

    def crear_usuario(self):
        print("\t\t Para iniciar,por favor registrese")
        self.usuario = input("\t\t Usuario: ")
        self._contraseña = input("\t\t Escriba su contraseña (Asegurese de encontrarse en un entorno seguro): ")
        return self.usuario 
    




