#Импорт
from flask import Flask, render_template, request, redirect, url_for, session
#Подключение библиотеки баз данных
from flask_sqlalchemy import SQLAlchemy
from password import gen_pass
from speakAI import *
import datetime
app = Flask(__name__)
#Подключение SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#Создание db
db = SQLAlchemy(app)
#Создание таблицы

class Card(db.Model):
    #Создание полей
    #id
    id = db.Column(db.Integer, primary_key=True)
    #Заголовок
    title = db.Column(db.String(100), nullable=False)
    #Описание
    subtitle = db.Column(db.String(300), nullable=False)
    #Текст
    text = db.Column(db.Text, nullable=False)

    #Вывод объекта и id
    def __repr__(self):
        return f'<Card {self.id}>'
    

#Задание №1. Создать таблицу User
class User(db.Model):
    #Создание полей
    #id
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    login = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(30), nullable=False)
#Запуск страницы с контентом
@app.route('/', methods=['GET','POST'])
def login():
        error = ''
        if request.method == 'POST':
            form_login = request.form['email']
            form_password = request.form['password']
            
            #Задание №4. Реализовать проверку пользователей
            users_db = User.query.all()
            for user in users_db:
                if form_login == user.login and form_password == user.password:
                    return redirect('/index')
            else:
                error = 'Неправильно указана почта или пароль'
                return render_template('login.html', error=error)
        else:
            return render_template('login.html')


@app.route('/reg', methods=['GET', 'POST'])
def reg():
    password_gen = gen_pass(10)
    
    if request.method == 'POST':
        login = request.form['email']
        password = request.form['password']
        # Задание №3. Реализовать запись пользователей
        user = User(login=login, password=password)
        db.session.add(user)
        db.session.commit()
    
    return render_template('registration.html', password_gen=password_gen)



#Запуск страницы с контентом
@app.route('/index')
def index():
    #Отображение объектов из БД
    cards = Card.query.order_by(Card.id).all()
    current_date_time = datetime.datetime.now()
    current_time = current_date_time.time()
    return render_template('index.html', cards=cards, current_time = current_time)

#Запуск страницы c картой
@app.route('/card/<int:id>')
def card(id):
    card = Card.query.get(id)

    return render_template('card.html', card=card)

#Запуск страницы c созданием карты
@app.route('/create')
def create():
    return render_template('create_card.html')

#Форма карты
@app.route('/form_create', methods=['GET','POST'])
def form_create():
    if request.method == 'POST':
        title =  request.form['title']
        subtitle =  request.form['subtitle']
        text =  request.form['text']

        #Создание объкта для передачи в дб

        card = Card(title=title, subtitle=subtitle, text=text)

        db.session.add(card)
        db.session.commit()
        return redirect('/index')
    else:
        return render_template('create_card.html')

@app.route('/voice_ru')
def voices_ru():
    text_ru = speak_ru()
    return render_template('create_card.html', text_ru = text_ru)


@app.route('/voice_en')
def voices_en():
    text_eng = speak_eng()
    return render_template('create_card.html', text_eng = text_eng)





if __name__ == "__main__":
    app.run(debug=True)