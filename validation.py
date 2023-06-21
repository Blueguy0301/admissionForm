from db import db
from textFieldNames import form1,form2,startUI
columns = [*startUI,*form1,*form2]
database = db()
databaseName = "collegeform"
# anong error dito?
# database.createDatabase(host="localhost",username="root",password="")

database.connect(host="localhost",username="root",password="",databaseName=databaseName)
tableName="admissionsystem"
def validate (data :dict): 
    result = database.create(column_names=columns,data=[*data.values()],tableName=tableName)

    print(result)
    pass