import os
import os.path
import write.condefine as cf
import config as conf

def modelwrite (tabletotal):
	path = 'java\\'+cf.classname+'\\' +cf.classname+ cf.modelfile
	isExists=os.path.exists(path)
	if not isExists:
		print (path+' 创建成功')
	else:
		print (path+' 目录已存在')
		f = open('java\\'+ cf.classname+'\\' +cf.classname+ cf.modelfile,"r+")
		read_data = f.read()
		f.seek(0)
		f.truncate()
		f.close()
	f1 = open('java\\'+ cf.classname+'\\' +cf.classname + cf.modelfile,'a') 
	str = cf.modelpackage + " " + conf.packagetxt + "model;"
	f1.write (str + '\n')
	f1.write ('\n')
	str = "public class " + cf.classname + " {"
	f1.write (str + '\n')
	for x in tabletotal:
		if x[2]=='NUMERIC' or x[2] == 'SERIAL':
			str = "private int " + x[0] + ";"
		else :
			str = "private String " + x[0] + ";"
		f1.write ('\t' + str + '\n')
	for x in tabletotal:
		if x[2]=='NUMERIC' or x[2] == 'SERIAL':
			spl = x[0][0].upper()+x[0][1:]
			str = "public int get" + spl + "() {"
			f1.write ('\t' + str + '\n')
			str = "return " + x[0] + "() {"
			f1.write ('\t\t' + str + ';\n}')
			str = "public void set" + spl + "(int "
			str += x[0] +") {"
			f1.write ('\t' + str + '\n')
			str = "this." + x[0] + " = " + x[0]
			f1.write ('\t\t' + str + ';\n}')
		else :
			spl = x[0][0].upper()+x[0][1:]
			str = "public String get" + spl + "() {"
			f1.write ('\t' + str + '\n')
			str = "return " + x[0]
			f1.write ('\t\t' + str + ';\n\t}\n')
			str = "public void set" + spl + "(String "
			str += x[0] +") {"
			f1.write ('\t' + str + '\n')
			str = "this." + x[0] + " = " + x[0]
			f1.write ('\t\t' + str + ';\n\t}\n')
			
	f1.write ('}')
	f1.close()