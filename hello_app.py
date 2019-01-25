from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

@app.route('/hello',methods =['POST'])
def hello():
    msg = request.get_json(force=True)
    name= msg['name']
    response = {
        'greeting' : 'Hello ,' +name +'!'
    }
    return jsonify(response)

if __name__=="__main__":
    print("Server is running at localhost")
    app.run(debug = True)
