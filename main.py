#Импорт
from flask import Flask, render_template,request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), nullable=False)
    text = db.Column(db.Text, nullable=False)
    
    def __repr__(self):
        return f'<Card {self}>'

#Запуск страницы с контентом
@app.route('/')
def index():
    return render_template('index.html')


#Динамичные скиллы
@app.route('/', methods=['POST'])
def process_form():
    if request.method == 'POST':
        button_python = request.form.get('button_python')
        button_telegram = request.form.get('button_telegram')
        button_html = request.form.get('button_html')
        button_db = request.form.get('button_db')
        return render_template('index.html', button_python=button_python, button_telegram=button_telegram, button_db=button_db, button_html=button_html)
    else:
        return redirect('index.html')
@app.route('/user_forma', methods=['POST', 'GET'])
def form():
    if request.method == 'POST':
        email = request.form.get('email')
        text = request.form.get('text')
        card = Card(email=email, text=text)
        db.session.add(card)
        db.session.commit()
        return render_template('user_form.html', email=email, text=text)
    else:
        return redirect('index.html') 

if __name__ == '__main__':
    app.run(debug=True)