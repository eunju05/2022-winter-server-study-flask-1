from flask import Flask, jsonify, request    #1. flask를 사용하기 위해 Flask class를 import

app = Flask(__name__)       #import한 flask 객체를 instantiate(인스턴스화) 시킨다.

#json 데이터를 보내어 이름만 반환 받는 POST 방식 API 
@app.route('/id', methods = ['POST'])   #route 데코레이터를 사용하여 엔드포인트 등록
def post():
    params = request.get_json()     #body에 입력한 정보를 받아
    Pdic = {}
    Pdic['name'] = params['name']   #dictionary에 key, value로 저장
    return Pdic                     #플라스크에서 딕셔너리로 리턴하면 알아서 json으로 변환

#ID값을 보내어 검증 받는 GET 방식 API
@app.route('/id/<int:id>', methods = ['GET'])   #route 데코레이터를 사용하여 엔드포인트 등록
def get(id):
    dic = {}
    if id >= 5000:                  #주소의 id가 5000이상이면
        dic['result'] = 'true'      #key : result, value : true
        return dic
    else :                          #주소의 id가 5000미만이면
        dic['result'] = 'false'     #key : result, value : false
        return dic                  #플라스크에서 딕셔너리로 리턴하면 알아서 json으로 변환

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)