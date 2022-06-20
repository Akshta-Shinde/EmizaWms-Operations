import mysql.connector

mydb = mysql.connector.connect(
  host="emiza-wms-dev-cluster-instance-1.c6238j2gf42s.ap-south-1.rds.amazonaws.com",
  user="emiza_wms_admin",
  password="EmizaWms$5678",
  database="factoryModal"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT dtm.HTMLText FROM DisplayTitleMaster dtm INNER JOIN ModuleStages ms ON dtm.ID = ms.DisplayTitleID WHERE ms.ID = '120100'")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)