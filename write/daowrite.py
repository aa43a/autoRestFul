import os
import os.path
import write.condefine as cf
import config as conf

def daowrite (tabletotal):
	path = 'java\\'+cf.classname+'\\' +cf.classname+ cf.daofile
	isExists=os.path.exists(path)
	if not isExists:
		print (path+' 创建成功')
	else:
		print (path+' 目录已存在')
		f = open('java\\'+ cf.classname+'\\' +cf.classname+ cf.daofile,"r+")
		read_data = f.read()
		f.seek(0)
		f.truncate()
		f.close()
	f1 = open('java\\'+ cf.classname+'\\' +cf.classname+ cf.daofile,'a') 
	str = cf.modelpackage + " " + conf.packagetxt + "dao;"
	f1.write (str + '\n')
	f1.write ('\n')
	for x in cf.daolines:
		f1.write(x)
	f1.write ('\n\n')
	f1.write ('import ' + conf.packagetxt + cf.xmlmodel + cf.classname)
	f1.write (';\n\n')
	f1.write ('@Repository\n')
	f1.write ('public interface ' + cf.classname + "Dao {")
	f1.write ('\n\t')
	f1.write ('void '+ cf.xmlinsert + cf.classname)
	f1.write ('('+cf.classname+ ' ' + cf.classname[0].lower() + cf.classname[1:] + ');')
	f1.write ('\n\t')
	f1.write ('void '+ cf.xmlupdate + cf.classname)
	f1.write ('(@Param("'+conf.xmlitem+'")'+cf.classname+ ' ' + cf.classname[0].lower() + cf.classname[1:] + ');')
	f1.write ('\n\t')
	f1.write ('void '+ cf.xmldelete + cf.classname)
	f1.write ('(String uniqueNums[]);')
	f1.write ('\n\t')
	f1.write ('List<'+ cf.classname + '> '+ cf.xmlselect + cf.classname)
	f1.write ('(@Param("'+tabletotal[0][0]+'")String ' + tabletotal[0][0])
	f1.write (');\n')
	f1.write ('}')