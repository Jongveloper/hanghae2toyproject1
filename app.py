from flask import Flask, render_template, request, jsonify, redirect, session, url_for, flash
from pymongo import MongoClient
app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbhanghae2

#처음 페이지(로그인)
@app.route('/')
def login():
    return render_template('login.html')

#회원가입 구현
app.config["SECRET_KEY"] = "hanghaehae"
@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template("sign_up.html")
    else:
        username = request.form['username']
        userid = request.form['userid']
        password = request.form['password']
        re_password = request.form['re_password']

        doc = {'user_id': userid, 'user_name': username, 'user_pw': password}

        if username == '' or userid == '' or password == '' or re_password == '':
            flash('모두 입력해주세요.')
            return render_template("sign_up.html")

        if password != re_password: # 비밀번호가 일치하지않을 때
            flash('비밀번호가 일치하지 않습니다.')
            return render_template("sign_up.html")
        else:
            db.hht1users.insert_one(doc)
            return redirect(url_for('login'))



if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)