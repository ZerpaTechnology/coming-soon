# -*- coding: utf-8 -*-
try:
 from modulos.ztec.zdb import DB
except:
 from zdb import DB
db=DB()
db.load=True
db('Usuarios').campo('Nombre',db.str,False,True,False,False,0,-1,None,None)
db('Usuarios').campo('Contenido',db.list,False,True,False,False,0,-1,None,None)
db('Usuarios').campo('args',db.dict,False,True,False,False,0,-1,None,None)
db('Usuarios').campo('Fecha',db.str,False,True,False,False,0,-1,None,'%d/%m/%Y %H:%M:%S')
db('Usuarios').campo('Status',db.list,False,True,False,False,0,-1,None,None)
db('Opciones').campo('Nombre',db.str,False,True,False,False,0,-1,None,None)
db('Opciones').campo('Valores',db.list,False,True,False,False,0,-1,None,None)
db('Opciones').insertar('Permisos', ['Administrador', 'Editor', 'Autor', 'Colaborador', 'Subscriptor'])
db.load=False
