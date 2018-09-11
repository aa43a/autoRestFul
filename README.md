# autoRestFul
give a create table sql auto generate restful and process file
=======
py autoRestFul.py

 process 
 Table.java              ---model <br>  
 TableDao.xml            ---mybatis xml <br>  
 TableDao.java           ---Dao <br>  
 TableService.java       ---Service interface <br>  
 TableServiceImpl.java   ---ServiceImpl  <br>  
 TableResource.java      ---Resource RestfulLink    @GET  @PUT  @POST  @DELETE /table/Table   <br>  

config.py

rootfile = "sql.txt"    //sql path <br>  
xmlitem = "item"        //variable param <br>  
packagetxt = "com.cqr.flansuka.process."   //package path   '.'is necessary  <br>  





