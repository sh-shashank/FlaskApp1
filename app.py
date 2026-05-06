from flask import Flask, redirect,request,render_template
import sqlite3

app=Flask(__name__)

# creating DB (first time only)
def init_db():
    conn=sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY, content TEXT)")
    conn.commit()
    conn.close
    
init_db()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add",methods=["POST"])
def add():
    note=request.form["note"]

    conn=sqlite3.connect("database.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO notes (content) VALUES (?)",(note,))
    conn.commit()
    conn.close()

    return redirect("/notes")

@app.route("/notes")
def notes():
    conn=sqlite3.connect("database.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM notes")
    data=cur.fetchall()
    conn.close()

    return render_template("notes.html",notes=data)

if __name__=="__main__":
    app.run()