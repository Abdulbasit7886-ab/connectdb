from flask import Flask
from flask import render_template,request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql ://root:@localhost/flask'
db = SQLAlchemy(app)

class form(db.Model):
    first_name = db.Column(db.String(80),primary_key=True )
    last_name = db.Column(db.String(80),nullable=False)
    email = db.Column(db.String(80),nullable=False)
    password = db.Column(db.String(80),nullable=False )
    contact = db.Column(db.Integer,nullable=False)

@app.route("/" ,methods=["GET","POST"])
def forms():
    if(request.method=='POST'):
        fname=request.form.get('fname')
        lname=request.form.get('lname')
        email=request.form.get('email')
        password=request.form.get('password')
        contact=request.form.get('contact')

        entry=form(first_name = fname,last_name=lname,email=email,password=password,contact=contact)
        db.session.add(entry)
        db.session.commit()

    return render_template('forms.html')

if __name__ =="__main__":
    app.run(debug=True)
