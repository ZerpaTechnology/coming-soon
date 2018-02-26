
from modulos.controlador import Controlador


class Portafolio(Controlador):
	def __init__(self,data,headers=None):

		Controlador.__init__(self,data,headers)

		
		

		self.vista="portafolio"
		
		
	
		
		if data["metodo"]==None  and data["action"]==None:
			
			self.servir()
		self.modelo=data["model"]["paginas"]
		

	def acerca(self):
		self.add_vista("acerca")
		self.servir()

	def test(self):
		self.add_vista("test")
		self.servir()

	def detalles(self):
		self.add_vista("Detalle")
		self.servir()
	def divi(self):
		
		self.add_vista("divi")
		self.servir()
	def divi_front(self):
		
		self.add_vista("divi-front")
		self.servir()

	
	





		
		