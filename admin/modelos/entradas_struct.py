db=DB()
db('Entradas').campo('Nombre',db.str,False,True,False,False,0,-1,None,None)
db('Entradas').campo('Contenido',db.list,False,True,False,False,0,-1,None,None)
db('Entradas').campo('args',db.dict,False,True,False,False,0,-1,None,None)
db('Entradas').campo('Fecha',db.str,False,True,False,False,0,-1,None,'%d/%m/%Y %H:%M:%S')
db('Entradas').campo('Status',db.list,False,True,False,False,0,-1,None,None)