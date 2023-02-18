from sqlalchemy import create_engine
from flask import make_response

class user_model():
    def __init__(self):
        try:
            self.con = create_engine('sqlite:///data12.db')
            self.con.autocommit = True        
            print("Connection Sucessful")
        except:
            print("Error")
    def get(self):
        #Business logic
        return make_response({"message":"Service is up"},201)

    def getall_task(self):
        #Business logic
        query = self.con.execute("Select * from data12")
        res= {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        if len(res)>0 :
            res = make_response({"payload":res},200)
            res.headers['Access-Control-Allow-Origin']="*"
            return res
        else:
            return  make_response({"message":"No Data Found"},201)

    def user_create_task(self,data):
        print(data)
        query = self.con.execute(f"INSERT INTO data12(ID,Task,Status) VALUES('{data['ID']}', '{data['Task']}', '{data['Status']}')")
        return make_response({"message":"CREATED_SUCCESSFULLY"},201)
    
    def add_multiple_task_model(self, dataa):
        # Generating query for multiple inserts
        qry = "INSERT INTO data12 (ID,Task,Status) VALUES"
        for data in dataa:
            #print(data)
            qry += f"('{data['ID']}', '{data['Task']}', '{data['Status']}'),"
        finalqry = qry.rstrip(",")
        query =self.con.execute(finalqry)
        return make_response({"message":"CREATED_SUCCESSFULLY"},201)
    
    def user_update_task(self,data):
        #print(data['Task'])
        #print(data['Status'])
        
        query12 = self.con.execute(f"Update data12 set Status='{data['Status']}' Where Task='{data['Task']}'")
        return make_response({"message":"UPDATED_SUCCESSFULLY"},201)
    
    def user_delete_task(self,data):
        print(data)
        query = self.con.execute(f"Delete from data12 Where Task='{data['Task']}'")
        return make_response({"message":"Deleted_SUCCESSFULLY"},201)
    
    def mark_task_complete(self, data):
        print(data)
        query = self.con.execute(f"Update data12 set Status='{'Complete'}' Where Task='{data['Task']}'")
        return make_response({"message":"UPDATED_SUCCESSFULLY"},201)
    
    def mark_task_incomplete(self, data):
        print(data)
        query = self.con.execute(f"Update data12 set Status='{'Incomplete'}' Where Task='{data['Task']}'")
        return make_response({"message":"UPDATED_SUCCESSFULLY"},201)
    