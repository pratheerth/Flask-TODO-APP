from flask import Flask, render_template , request , redirect ,url_for
from tinydb import TinyDB, Query
import random

app = Flask(__name__)
db = TinyDB('db.json')


@app.route("/")
def root():
    todo_list = db.all()
    return render_template('index.html',todo_list=todo_list)

@app.route("/add",methods=["POST"])
def add():
    title = request.form.get("title")
    db.insert({'id':random.randint(0, 1000),'title': title, 'complete': False})
    return redirect(url_for("root"))

@app.route("/update",methods=["POST"])
def update():
    todo_db = Query()
    newTest = request.form.get('inputField')
    todo_id =  request.form.get('hiddenField')
    db.update({"title": newTest},todo_db.id == int(todo_id))
    return redirect(url_for("root"))

@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    todo_db = Query()
    db.remove(todo_db.id == todo_id)
    return redirect(url_for("root"))

@app.route("/complete/<int:todo_id>")
def complete(todo_id):
    todo_db = Query()
    db.update({"complete": True},todo_db.id == todo_id)
    return redirect(url_for("root"))
    

if __name__ == '__main__':
    app.run(debug=True)
