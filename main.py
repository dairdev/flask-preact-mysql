from flask import current_app, flash, Flask, Markup, redirect, render_template, request

app = Flask(__name__)
app.debug = False
app.testing = False

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html', usuario='test')


@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return index()
    else:
        return render_template('home.html', usuario=request.form['user'] )


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
