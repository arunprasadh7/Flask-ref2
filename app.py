from flask import Flask,render_template

app = Flask(__name__)


@app.route('/hello')
def index():
    return 'Hello World!!'

@app.route('/')
def hi():
    user = {
        'name' :'Arun',
        'city' : 'Coimbatore',
    }
    views = 568
    return render_template('home.html',user=user,views=views)


if __name__ == '__main__':
    app.run(debug=True)