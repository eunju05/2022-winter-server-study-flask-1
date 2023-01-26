from flask import Flask, jsonify, request     #1. flask를 사용하기 위해 Flask class를 import

app = Flask(__name__)       #import한 flask 객체를 instantiate(인스턴스화) 시킨다.

@app.route('/id', methods = ['POST'])   #route 데코레이터를 사용하여 엔드포인트 등록
def home():
    params = request.get_json()
    user_name = jsonify(params['name'])
   
    return user_name

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)