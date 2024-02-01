from flask import Flask ,request
from markupsafe import escape #used to prevent injection attacks/ reduces security risk of script injection 

app  = Flask(__name__)

@app.route('/')
def home():
    return 'Hello World!'

# string - default is string 
@app.route('/hello/<name>')
def greet(name):
    return f'<h1>Hello {name}</h1>'

# int 
@app.route('/age/<int:age>')
def user_age(age):
    return f' Your age is : {age}'

# float 
@app.route('/height/<float:height>')
def height(height):
    return f' Your height is : {height} '

# path - url after the route will be assigned to variable
@app.route('/path/<path:urlPath>')
def path(urlPath):
    return f'Entered url path is : \'{urlPath}\''


# escape demo 
@app.route('/safename/<name>')
def escape_demo(name):
    safename = escape(name)
    return f'Your name is {safename}.'


# Using query parameter 
@app.route('/search')
def query():
    q = request.args.to_dict()
    return f'Hello {q.get('uname','No Name')}'



if __name__ == '__main__':
    app.run(debug=True) 