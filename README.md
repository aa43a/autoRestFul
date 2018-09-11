# autoRestFul
give a create table sql auto generate restful and process file
---------
Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
<br> 
sql  base postgresql<br> <br>  
py autoRestFul.py

<br>  
 process <br>  
 Table.java              ---model <br>  
 TableDao.xml            ---mybatis xml <br>  
 TableDao.java           ---Dao <br>  
 TableService.java       ---Service interface <br>  
 TableServiceImpl.java   ---ServiceImpl  <br>  
 TableResource.java      ---Resource RestfulLink    @GET  @PUT  @POST  @DELETE /table/Table   <br>  
<br>  
<br>  
config.py <br>  
<br>  
<br>  
rootfile = "sql.txt"    //sql path <br>  
xmlitem = "item"        //variable param <br>  
packagetxt = "com.cqr.flansuka.process."   //package path   '.'is necessary  <br>  





