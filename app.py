from flask import Flask, render_template, request, redirect, session, url_for
from cs50 import SQL
from datetime import datetime, date
from flask_session import Session
db=SQL("sqlite:///journal_entry.db")


app=Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
app.secret_key = 'dfudsahgihdso'


@app.route("/index")
def index():
    user = db.execute("SELECT * FROM users WHERE username = ?", session.get("username"))
    if not user:
        return redirect("/")
    user_id = user[0]["id"]

    emotion_log = db.execute("SELECT date, emotion FROM emotions WHERE user_id = ? ORDER BY date", user_id)

    return render_template("index.html", emotion_log=emotion_log)


@app.route('/register', methods=['GET', 'POST'])
def register():
   if request.method == 'POST':
       username = request.form.get("username")
       password = request.form.get("password")

       existing = db.execute("SELECT * FROM users WHERE username = ?", [username])
       if len(existing) > 0:
           return "User already exists. <a href='/register'>Try again</a>"

       else:
           db.execute("INSERT INTO users (username, password) VALUES (?, ?)", username, password)
           return redirect("/")

   return render_template('register.html')


@app.route('/', methods=['GET', 'POST'])
def login():
   if request.method == 'POST':
       username = request.form.get("username")
       password = request.form.get("password")
       user = db.execute("SELECT * FROM users WHERE username = ? AND password = ?", username, password)

       if user:
           session['username'] = username
           session['id'] = user[0]['id']
           return redirect(url_for('index'))
       else:
           return "Invalid credentials. <a href='/login'>Try again</a>"

   return render_template('login.html')


@app.route('/logout')
def logout():
   session.clear()
   return redirect("/")


@app.route("/journal", methods=["GET"])
def journal():
    user_id = session.get("id")
    if not user_id:
        return redirect("/")

    journal_table = db.execute("SELECT * FROM journal_table WHERE user_id = ? ORDER BY timestamp DESC", user_id)

    for entry in journal_table:
        dt = datetime.strptime(entry['timestamp'], "%Y-%m-%d %H:%M:%S")
        entry['formatted_date'] = dt.strftime("%B %d, %Y")

    return render_template("journal.html", journal_table=journal_table)


@app.route("/delete", methods = ["GET"])
def delete():
    if request.method == "GET":
        id = request.args.get("id")

        db.execute ("DELETE FROM journal_table WHERE id=?",id)
        return redirect("/journal")


@app.route("/tracker", methods=["GET", "POST"])
def tracker():
    user = db.execute("SELECT * FROM users WHERE username = ?", session.get("username"))
    if not user:
        return redirect("/")
    user_id = user[0]["id"]
    today = date.today().isoformat()

    submitted = False
    emotion = 0

    if request.method == "POST":
        existing = db.execute("SELECT * FROM emotions WHERE user_id = ? AND date = ?", user_id, today)
        if not existing:
            emotion = int(request.form.get("emotion"))
            db.execute("INSERT INTO emotions (user_id, date, emotion) VALUES (?, ?, ?)", user_id, today, emotion)
        submitted = True

    else:
        existing = db.execute("SELECT * FROM emotions WHERE user_id = ? AND date = ?", user_id, today)
        if existing:
            submitted = True
            emotion = existing[0]["emotion"]

    # emotion_log is optional, in case you want to display a chart later
    emotion_log = db.execute("SELECT date, emotion FROM emotions WHERE user_id = ? ORDER BY date", user_id)

    return render_template("tracker.html", emotion=emotion, submitted=submitted, emotion_log=emotion_log)


@app.route("/journal_page", methods=["GET", "POST"])
def journal_page():
    if request.method == "GET":
        return render_template("journal_page.html")

    if request.method == "POST":
        title = request.form.get("title")
        entry = request.form.get("entry")

        # Get user ID from session
        user_id = session.get("id")
        if not user_id:
            return redirect("/")

        # Insert with user_id
        db.execute("INSERT INTO journal_table (user_id, title, journal_entry) VALUES (?, ?, ?)", user_id, title, entry)

        return redirect("/journal")


@app.route("/entry/<int:entry_id>")
def view_entry(entry_id):
    entry = db.execute("SELECT * FROM journal_table WHERE id = ?", entry_id)

    entry = entry[0]

    dt = datetime.strptime(entry['timestamp'], "%Y-%m-%d %H:%M:%S")
    entry['formatted_date'] = dt.strftime("%B %d, %Y")

    return render_template("view_entry.html", entry=entry)


if __name__ == "__main__":
    app.run()
