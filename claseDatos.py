class Informacion:
    def mi_lista(self):
        lista_NombrePerros = ["Boby", "Dollar", "Fany"]
        for x in lista_NombrePerros:
            print(x)
    def mi_tupla(self):
        lista_razaPerros = ("pastor aleman", "bulldog", "Beagle")
        for x in lista_razaPerros:
            print(x)
    def mi_diccionario(self):
        lista_informacion = {"color": "negro", "nombre": "Pedro", "raza":"pastor aleman"}
        for x, key in lista_informacion.items():
            print(x,": " ,key) 
    def mi_conjunto(self):
        lista_tiposMascotas = {"gatos", "perro", "tortuga"}
        for x in lista_tiposMascotas:
            print(x)
# creando el objeto
datos = Informacion()
print("---------------------")
print("Lista")
print("\nListado de nombres de perros ")
datos.mi_lista()

print("---------------------")
print("tupla")

print("\nListado de razas de perros")
datos.mi_tupla()

print("---------------------")
print("diccionario")
print("\nListado de informacion de perros ")
datos.mi_diccionario()

print("---------------------")
print("conjunto")
print("\nListado de tipos de mascotas ")
datos.mi_conjunto()




