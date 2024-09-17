print("Clases version 2 el constructor")
class Perro:
    # Funcion constructor
    def __init__(self, color, edad):
        self.color = color
        self.edad = edad
    # fUNCIONES CREADAS POR EL USUARIO
    def muerde(self):
        print("Chale el perro me mordió")

    def chatPerro(self, mensaje):
        print(f"Chat perro: {mensaje}")

    def chatperra(self, mensajepe):
        print(f"Chat perra: {mensajepe}")
    def datos(self):
        print(f"Color: {self.color}, edad: {self.edad}")
# Crear el objeto  
chihuas = Perro("Negro", 2)

# Llamando a funciones
chihuas.datos() 
chihuas.muerde()
chihuas.chatPerro("Hola canina")
chihuas.chatperra("Hola boby")
chihuas.chatPerro("¿Quieres ser mi novia?")
chihuas.chatperra("Grrru......")
