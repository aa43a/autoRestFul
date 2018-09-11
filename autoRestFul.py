import write.xmlwrite as xw
import write.daowrite as dw
import write.modelwrite as mw
import write.servicewrite as sw
import write.serviceimplwrite as siw
import write.resourcewrite as rw
import os
import os.path
import write.condefine as cf
import config as conf


f = open(conf.rootfile,encoding='utf8') 
line = f.readline()

def formatName( str ):
	stringList = str.split('_')
	stringListAfter= []
	i=0;
	for x in  stringList:
		if i != 0:
			stringListAfter.append(x.capitalize())
		else :
			stringListAfter.append(x)
		i+=1
	return ''.join(stringListAfter)
	
def formatClassName( str ):
	stringList = str.split('_')
	stringListAfter= []
	for x in  stringList:
		stringListAfter.append(x.capitalize())
	return ''.join(stringListAfter)
	

while line:
	
	if  line.startswith(cf.startswithstr) and line.split( )[1] == cf.table:
		cf.tableflag=True
		cf.classnamebefore = cf.classname = line.split( )[2]
		cf.classname = formatClassName(cf.classname)
		print(cf.classname)
		print(cf.classnamebefore)
	elif  line.startswith(cf.endtablestr):
		if len(cf.tablelisttotal) > 0 :
			cf.tableflag=False
			path = 'java\\'+cf.classname
			isExists=os.path.exists(path)
			if not isExists:
				os.makedirs(path) 
				print (path+' 创建成功')
			else:
				print (path+' 目录已存在')
			xw.xmlwrite (cf.tablelisttotal)
			mw.modelwrite (cf.tablelisttotal)
			dw.daowrite (cf.tablelisttotal)
			sw.servicewrite(cf.tablelisttotal)
			siw.serviceimplwrite(cf.tablelisttotal)
			rw.resourcewrite(cf.tablelisttotal)
			cf.tablelisttotal = []
	elif  cf.tableflag == True:
		cf.tablelist = line.split( )
		if cf.tablelist[0] != cf.columnexpert:
			cf.tablelist.append(cf.tablelist[2])
			cf.tablelist[2] = cf.tablelist[1]
			cf.tablelist[1] = cf.tablelist[0]
			cf.tablelist[0] = formatName(cf.tablelist[1])	
			cf.tablelisttotal.append(cf.tablelist)				
		
	line = f.readline()
	

	

