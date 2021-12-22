from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = "shhhh"

@app.route('/')
def form_blank():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def form_filled():
    print("Got survey info")
    session['username'] = request.form['name']
    session['dojolocation'] = request.form['location']
    session['favlang'] = request.form['lang']
    session['usercomment'] = request.form['comment']
    return redirect('/result')

@app.route('/result')
def return_form():
    return render_template('show.html')

if __name__ == "__main__":
    app.run(debug=True)