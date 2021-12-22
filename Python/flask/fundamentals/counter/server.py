from flask import Flask, render_template, redirect, session
app = Flask(__name__)
app.secret_key = "shhhhh"

@app.route('/')
def counter():
    if 'count' not in session:
        session['count'] = 0
    else:
        session['count'] += 1
    return render_template("index.html")

@app.route('/plustwo')
def addtwo():
    if 'count' not in session:
        session['count'] = 0
    else:
        session['count'] += 1
    return redirect("/")

@app.route('/destroy_session')
def destory_ses():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)