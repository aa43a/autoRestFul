# autoRestFul
give a create table sql auto generate restful and process file

py autoRestFul.py

 process 
 Table.java              ---model
 TableDao.xml            ---mybatis xml
 TableDao.java           ---Dao
 TableService.java       ---Service interface
 TableServiceImpl.java   ---ServiceImpl 
 TableResource.java      ---Resource RestfulLink    @GET  @PUT  @POST  @DELETE /table/Table  

config.py

rootfile = "sql.txt"    //sql path
xmlitem = "item"        //variable param
packagetxt = "com.cqr.flansuka.process."   //package path   '.'is necessary





