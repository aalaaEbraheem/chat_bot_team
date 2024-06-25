from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from chatbot_response import chatbot_response
from waitress import serve
import speech_recognition as sr

app = Flask(__name__)
cors = CORS(app)

@app.route('/ChatBot', methods=['GET','POST'])
def chatbot():
    try:
        if request.method == "GET":
            msg = request.args.get('msg')
        elif request.method == "POST":
            body = request.json
            msg = body["msg"]
    except:
        return jsonify({'answer': "An ERROR OCCURED"}) , 200
    
    if len(msg) < 2 :
        return jsonify({'answer': "Please Send Valid Msg"}) , 200
     
    answer = chatbot_response(msg)
    print(msg)
    return jsonify({'answer': answer}) , 200

def run_server():
        print("Application Run Successfully.... :)")
        app.run(host='0.0.0.0', port=5000)

run_server()

# while True:
#     qs = input("enter you question")
#     print (chatbot_response(qs))