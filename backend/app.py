from flask import Flask, render_template, redirect, url_for, flash
from flask_migrate import Migrate
from forms import TransactionForm
from models import db, Transaction
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://Mereke:Jennifer_107@localhost/form_react'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'key'

db.init_app(app)
migrate = Migrate(app, db)


@app.route('/')
def index():
    transactions = Transaction.query.all()
    print(transactions)
    return render_template('index.html', transactions=transactions)
   
@app.route('/add_transaction', methods=["GET", "POST"])  
def add_transaction():
    form = TransactionForm()
    if form.validate_on_submit(): 
        print("Success!")
        print("Form data:", form.data)
        try:
            if isinstance(form.dateTime.data, str):
                form.dateTime.data = datetime.strptime(form.dateTime.data, '%Y-%m-%dT%H:%M')   
            transaction = Transaction(author=form.author.data, sum=form.sum.data, category=form.category.data,
                                  comment=form.comment.data, dateTime=form.dateTime.data)
            db.session.add(transaction)
            db.session.commit()
            flash('Transaction added succesfully', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            db.session.rollback()
            flash(f"Error: {e}", 'danger')
    else:
        print("Form validation failed: ", form.errors)        
    return render_template('add_transaction.html', form = form)

    
if __name__ == '__main__':
    app.run(debug=True)    

