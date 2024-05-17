import sqlite3

db_name = 'quiz.db'
conn = None
cursor = None


def open():
    global conn, cursor
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()


def close():
    cursor.close()
    conn.close()


def do(query):
    cursor.execute(query)
    conn.commit()


def create():
    open()
    do('''CREATE TABLE quiz(
        id INTEGER PRIMARY KEY,
        name VARCHAR)''')
    
    do('''CREATE TABLE questions(
        id INTEGER PRIMARY KEY,
        question VARCHAR,
        answer VARCHAR,
        wrong1 VARCHAR,
        wrong2 VARCHAR,
        wrong3 VARCHAR)''')
    
    do('''CREATE TABLE quiz_content(
        id INTEGER PRIMARY KEY,
        quiz_id INTEGER,
        question_id INTEGER,
        FOREIGN KEY(quiz_id) REFERENCES quiz(id),
        FOREIGN KEY(question_id) REFERENCES questions(id))''')
    
    close()


def clear_db():
    ''' видаляє всі таблиці '''
    open()
    query = '''DROP TABLE IF EXISTS questions'''
    do(query)
    query = '''DROP TABLE IF EXISTS quiz'''
    do(query)
    query = '''DROP TABLE IF EXISTS quiz_content'''
    do(query)
    close()


def add_quizes():
    open()
    quizes = [
        ('Алгебра',),
        ('Історія',),
        ('Біологія',)
    ]
    cursor.executemany('''INSERT INTO quiz (name) VALUES(?)''', quizes)
    conn.commit()
    close()


def add_questions():
    open()
    questions = [
        ('Як називається алгебраїчний вираз, що має однаковий змінний множник?',
         'Моном',
         'Частковий дріб',
         'Функція',
         'Множина',),
        ('Скільки буде 7 в 3 степені?',
         '343',
         '49',
         '21',
         '511',),
        ('Розв`яжіть рівняння: 2x+5=17',
         'x = 6',
         'x = 5',
         'x = 4',
         'x = 3',),
        ('Скільки граней у куба?',
         '6',
         '8',
         '12',
         '4',),
        ('Розв`яжіть нерівність: 5-2x>1',
         'x < 2',
         'x > 2',
         'x > 3',
         'x < 6',),
        ('Хто був першим президентом США?',
         'Джордж Вашингтон',
         'Авраам Лінкольн',
         'Франклін Рузвельт',
         'Джон Кеннеді',),
        ('В якому році відбулася битва при Ватерлоо?',
         '1815',
         '1812',
         '1832',
         '1842',),
        ('Хто був останнім імператором Російської імперії?',
         'Микола II',
         'Петро III',
         'Олександр II',
         'Павло I',),
        ('В якому році відбувся перший політ людини в космос?',
         '1961',
         '1943',
         '1968',
         '1999',),
        ('Хто був автором "Декларації незалежності" США?',
         'Томас Джефферсон',
         'Джеймс Медісон',
         'Джордж Вашингтон',
         'Джон Адамс',),
        ('Який орган у людини відповідає за фільтрацію крові?',
         'Нирки',
         'Печінка',
         'Серце',
         'Легені',),
        ('Що таке процес, за якого зелені рослини виробляють свою їжу?',
         'Фотосинтез',
         'Дихання',
         'Дендрит',
         'Ферментация',),
        ('Який вуглевод є основним джерелом енергії для організму?',
         'Глюкоза',
         'Сахароза',
         'Лактоза',
         'Фруктоза',),
        ('Яка структура є основною одиницею спадкової інформації в організмі?',
         'Ген',
         'Клітина',
         'Хромосома',
         'Білок',),
        ('Яка частина клітини відповідає за синтез білків?',
         'Рибосоми',
         'Мітохондрії',
         'Лізосоми',
         'Білки',),
    ]
    cursor.executemany('''INSERT INTO questions (question, answer, wrong1, wrong2, wrong3) VALUES(?, ?, ?, ?, ?)''', questions)
    conn.commit()
    close()

def add_link():
    open()
    cursor.execute('''PRAGMA foreign_keys=on''')
    answer = input("Додати зв'язок? (y/n)")
    while answer != 'n':
        quiz_id = int(input("Введіть номер вікторини:"))
        question_id = int(input("Введіть номер запитання:"))
        cursor.execute('''INSERT INTO quiz_content(quiz_id, question_id) VALUES(?, ?)''', [quiz_id, question_id])
        conn.commit()
        answer = input("Додати зв'язок? (y/n)")

    close()

def main():
    # clear_db()
    # create()
    # add_quizes()
    # add_questions()
    add_link()
    


main()