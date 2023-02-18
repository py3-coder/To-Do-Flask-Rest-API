from flask import Flask, make_response, request
from flask import request
from model import user_model

app = Flask(__name__)

obj =user_model()

@app.route("/")
def home():
    return make_response({"message":"Welcome to TO-DO Flask API"},201)

@app.route("/get",methods=['GET'])
def get():
    return obj.get()

@app.route("/user/getall",methods=['GET'])
def getall_controller():
    return obj.getall_task()

@app.route("/user/create",methods=["POST"])
def create():
    return obj.user_create_task(request.form)

@app.route("/user/create-multiple",methods=["POST"])
def create_multi():
    return obj.add_multiple_task_model(request.json)

@app.route("/user/update",methods=["POST"])
def update():
    return obj.user_update_task(request.form)

@app.route("/user/delete",methods=["DELETE"])
def delete():
    return obj.user_delete_task(request.form)

@app.route("/user/complete-task",methods=["POST"])
def update_complete():
    return obj.mark_task_complete(request.form)

@app.route("/user/incomplete-task",methods=["POST"])
def update_incomplete():
    return obj.mark_task_incomplete(request.form)

if __name__ == '__main__':
     app.run(debug=True,host='0.0.0.0',port=int(5000))



