xmlfile = "Dao.xml"
xmlmapper = "mapper "
xmlnamespace = "namespace "
xmlinsert = "insert"
xmlupdate = "update"
xmldelete = "delete"
xmlselect = "select"
xmlinto = "into"
xmlid = "id"
xmlequ = "="
xmlsqlparameterType = "parameterType"
xmlresultType = "resultType"
xmlset = "set"
xmlif = "if"
xmltest = "test"
xmlforeach = "foreach"
xmlend = "/"
xmlnot1 = " != null "
xmlnot2 = " != '' "
xmland = "and"
xmlcollection = "collection"
xmlitem = "item"
xmlopen = "open"
xmlseparator = "separator"
xmlclose = "close"
xmlDao ="Dao"
xmldao = "dao."
xmlsep = ","
xmlleft = "<"
xmlright = ">"
xmllsq = "("
xmlrsq = ")"
xmllm = "\""
xmlmodel = "model."
xmlvalues = "values"
xmlwhere = "where"
xmlfrom = "from"
xmlin = "in"
xmlas = "as"
xmlline = ['<?xml version="1.0" encoding="UTF-8"?>',
			'<!DOCTYPE mapper PUBLIC   ',
			'"-//mybatis.org//DTD Mapper 3.0//EN"  ',
			'"http://mybatis.org/dtd/mybatis-3-mapper.dtd">']
			
modelpackage = "package"

daolines = ['import java.util.List;',
			'\n\nimport org.apache.ibatis.annotations.Param;',
			'\nimport org.springframework.stereotype.Repository;']

resourcelines = ['import java.util.List;',
				 'import javax.ws.rs.DELETE;',
				 'import javax.ws.rs.GET;',
				 'import javax.ws.rs.POST;',
				 'import javax.ws.rs.PUT;',
				 'import javax.ws.rs.Path;',
				 'import javax.ws.rs.Produces;',
				 'import javax.ws.rs.QueryParam;',
				 'import javax.ws.rs.core.GenericEntity;',
				 'import javax.ws.rs.core.Response;',
				 'import javax.ws.rs.core.Response.Status;',
				 'import org.springframework.beans.factory.annotation.Autowired;',
				 'import org.springframework.stereotype.Component;']
				 
rootfile = "sql.txt"
modelfile = ".java"

resourcepath = "alarm"
daofile = "Dao.java"
servicefile = "Service.java"
serviceimplfile = "ServiceImpl.java"
resourcesfile = "Resource.java"
startswithstr = "create"
endtablestr = ");"
table = "table"
tablelist = []
tablelisttotal = []
packagetxt = "com.gmi.its.itsmain."
classname = ""
classnamebefore = ""
columnexpert = "constraint"
tableflag = False