db=DB()
db('Contactos').campo('Nombre',db.str,False,True,False,False,0,-1,None,None)
db('Contactos').campo('Contenido',db.list,False,True,False,False,0,-1,None,None)
db('Contactos').campo('args',db.dict,False,True,False,False,0,-1,None,None)
db('Contactos').campo('Fecha',db.str,False,True,False,False,0,-1,None,'%d/%m/%Y %H:%M:%S')
db('Contactos').campo('Status',db.list,False,True,False,False,0,-1,None,None)
db('Contactos').insertar('zerpatechnology', [[{'Nombre': 'text', 'name': 'titulo', 'value': 'zerpatechnology'}, {'Avatar': 'text', 'value': 'https://zerpatechnology.com.ve/tipo=avatar&imgs=jdym', 'name': 'avatar'}, {'name': 'conversaciones', 'value': [{'Tu': '', 'Yo': ''}], 'Conversaciones': 'textarea'}]], {'Contacto': 0}, '12/7/2017 10:27:11', [])