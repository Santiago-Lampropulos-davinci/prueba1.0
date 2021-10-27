import math

class Alumno(object):
	def __init__(self):
		self.nombre = ""
		self.contrasenia = ""
		self.carrera = None

	def crearAlumno(nombreAsignado, contraseniaAsignada):
		self.nombre = nombreAsignado
		self.contrasenia = contraseniaAsignada
		return self


	def asignarCarrera(carreraAsignada):
		self.carrera = carreraAsignada