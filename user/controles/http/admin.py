
from modulos.controlador import Controlador
from config import config
from settings import config as settings
import sys

from Controladores.http.admin import preLoad

def admin(data,headers=None):
	

	cnt=preLoad(data,headers)
	

	class Admin(cnt):
		def __init__(self,data,headers=None):
			
			cnt.__init__(self,data,headers)

			if self.data["metodo"]==None and self.data["ajax"]==False and self.data["action"] not in config.hookNotActions:
				self.servir()

		def index(self):
			self.servir()

		

		def licencias(self):
			self.vista="licencias"
			self.servir()


	return Admin(data,headers)