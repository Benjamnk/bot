from flask import Flask , request , abort

app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello BotBK' , 200


@app.route('/webhook',methods = ['POST','GET'])
def webhook():
    if request.method == 'POST':
        print(request.json)
        return request.json , 200
    
    elif request.method == 'GET':
        return 'this is MY Bot project ' , 200




