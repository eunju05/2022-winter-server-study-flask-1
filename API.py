from flask import Flask, jsonify, request    #1. flask를 사용하기 위해 Flask class를 import

app = Flask(__name__)       #import한 flask 객체를 instantiate(인스턴스화) 시킨다.

@app.route('/id', methods = ['POST'])   #route 데코레이터를 사용하여 엔드포인트 등록
def post():
    params = request.get_json()
    Pdic = {}
    Pdic['name'] = params['name']
    return Pdic

@app.route('/id/<int:id>', methods = ['GET'])   #route 데코레이터를 사용하여 엔드포인트 등록
def get(id):
    dic = {}
    if id >= 5000:
        dic[id] = 'true'
        return dic
    else :
        dic[id] = 'false'
        return dic

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)