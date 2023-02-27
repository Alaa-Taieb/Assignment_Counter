from flask import Flask, render_template, session, redirect,request

app = Flask(__name__)
app.secret_key = "Yeah .. that's secure"
@app.route('/')
def counter():
    if 'counter' not in session or 'visited' not in session:
        session['counter'] = 1
        session['visited'] = 1
    else:
        session['visited'] = session['visited'] + 1
        session['counter'] = session['counter'] + 1
    return render_template("index.html" , counter = session['counter'] , visited = session['visited'])

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')

@app.route('/plus_two')
def add_two():
    session['counter'] += 1
    return redirect('/')

@app.route('/add_custom', methods=['post'])
def add_custom():
    times = int(request.form['times']) 
    times -= 1
    session['counter'] += times
    return redirect('/')

if __name__ == "__main__":
    app.run(debug = True)