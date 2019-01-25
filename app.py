from flask import Flask,render_template
from flask import jsonify
from flask import request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hello',methods =['POST'])
def hello():
    msg = request.get_json(force=True)
    name= msg['name']
    response = {
        'greeting' : 'Hello ,' +name +'!'
    }
    return jsonify(response)


@app.route('/about')
def about():
    return("This is a test sample")


if __name__=="__main__":
    print("Server is running at localhost")
    app.run(debug = True)
