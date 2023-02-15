from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
DATABASE = 'nfl_quiz.db'

# Initialize database with questions
def init_db():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT,
            option1 TEXT,
            option2 TEXT,
            option3 TEXT,
            option4 TEXT,
            answer INTEGER
        );
    ''')
    c.execute('SELECT COUNT(*) FROM questions')
    count = c.fetchone()[0]
    if count == 0:
        c.execute('''
            INSERT INTO questions (question, option1, option2, option3, option4, answer)
            VALUES 
            ("What team won the first Super Bowl in NFL history?", "Dallas Cowboys", "Green Bay Packers", "Miami Dolphins", "Pittsburgh Steelers", 2),
            ("What team has the most Super Bowl wins?", "Pittsburgh Steelers", "Dallas Cowboys", "New England Patriots", "San Francisco 49ers", 3),
            ("What team won Super Bowl 50?", "Denver Broncos", "Carolina Panthers", "Seattle Seahawks", "New England Patriots", 1),
            ("What player has the most career passing yards in NFL history?", "Tom Brady", "Drew Brees", "Peyton Manning", "Brett Favre", 2),
            ("What team did the New England Patriots defeat to complete the first 19-0 perfect season?", "Pittsburgh Steelers", "Indianapolis Colts", "New York Giants", "Dallas Cowboys", 3)
        ''')
        conn.commit()
    conn.close()

# Display questions from database
@app.route('/')
def index():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('SELECT * FROM questions')
    questions = c.fetchall()
    conn.close()
    return render_template('index.html', questions=questions)

# Add new question to database
@app.route('/add', methods=['GET', 'POST'])
def add_question():
    if request.method == 'POST':
        question = request.form['question']
        option1 = request.form['option1']
        option2 = request.form['option2']
        option3 = request.form['option3']
        option4 = request.form['option4']
        answer = request.form['answer']
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        c.execute('INSERT INTO questions (question, option1, option2, option3, option4, answer) VALUES (?, ?, ?, ?, ?, ?)', (question, option1, option2, option3, option4, answer))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('add_question.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
