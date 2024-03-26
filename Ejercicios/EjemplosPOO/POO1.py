class Estudiante():
    def __init__ (self, nombre, apellidos, grupo, edad, nia):
       self.nombre = nombre
       self.apellidos = apellidos
       self.grupo = grupo 
       self.edad = edad 
       self.nia = nia

    def muestraInformacion (self):
        print ()
        print ('Nombre:', self.nombre)
        print ('Apellidos:', self.apellidos)    
        print ('Grupo:', self.grupo)
        print ('Edad:', self.edad)
        print ('NIA:', self.nia)

    def MayorEdad (self):
        if self.edad >= 18:
            print (True)
        else:
            print (False)

alumno1 = Estudiante('Antonio','Gómez García','4ESOA',16,12356788)
alumno2 = Estudiante('Ferran','Llach Folch','2BACHA',18,10772489)

alumno1.muestraInformacion()
alumno1.MayorEdad()

alumno2.muestraInformacion()
alumno2.MayorEdad()