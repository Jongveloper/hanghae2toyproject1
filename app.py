from flask import Flask, render_template, request, jsonify, redirect, session, url_for, flash
from pymongo import MongoClient
app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbhanghae2

#처음 페이지(로그인)
@app.route('/', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        userid = request.form['userid']
        password = request.form['password']
        users = db.hht1users.find_one({'user_id': userid, 'user_pw': password})
        if users is None:
            flash("아이디와 비밀번호를 확인해주세요.")
            # return "아이디와 비밀번호를 확인해주세요."
        else:
            session['user'] = userid
            return redirect('main')
        return redirect('/')

#메인 페이지
@app.route('/main')
def main():
    return render_template('main.html')

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
            flash('회원가입 완료')
            return redirect('/')

# 메모 구현 (POST API)(종혁)
@app.route('/memo', methods=['POST'])
def save_memo():
    memo = request.form['memo']

    doc = {'memo': memo}

    db.memo.insert_one(doc)

    return jsonify({'msg': '작성하기 완료!'})

# 메모 목록 보기 구현 (GET api)(종혁)
@app.route('/memo', methods=['GET'])
def view_memo():
    view = list(db.memo.find({}, {'_id': False}))
    return jsonify({'memo': view})

# 메모 구현 (POST API)(재인님)
@app.route('/jmemo', methods=['POST'])
def save_jmemo():
    jmemo = request.form['jmemo']

    doc = {'jmemo': jmemo}

    db.jmemo.insert_one(doc)

    return jsonify({'msg': '작성하기 완료!'})

# 메모 목록 보기 구현 (GET api)(재인님)
@app.route('/jmemo', methods=['GET'])
def view_jmemo():
    view = list(db.jmemo.find({}, {'_id': False}))
    return jsonify({'jmemo': view})

# 메모 구현 (POST API)(나영님)
@app.route('/nmemo', methods=['POST'])
def save_nmemo():
    nmemo = request.form['nmemo']

    doc = {'nmemo': nmemo}

    db.nmemo.insert_one(doc)

    return jsonify({'msg': '작성하기 완료!'})


# 메모 목록 보기 구현 (GET api)(나영님)
@app.route('/nmemo', methods=['GET'])
def view_nmemo():
    view = list(db.nmemo.find({}, {'_id': False}))
    return jsonify({'nmemo': view})

# 메모 구현 (POST API)(선민님)
@app.route('/smemo', methods=['POST'])
def save_smemo():
    smemo = request.form['smemo']

    doc = {'smemo': smemo}

    db.smemo.insert_one(doc)

    return jsonify({'msg': '작성하기 완료!'})


# 메모 목록 보기 구현 (GET api)(선민님)
@app.route('/smemo', methods=['GET'])
def view_smemo():
    view = list(db.smemo.find({}, {'_id': False}))
    return jsonify({'smemo': view})

#종혁님 개인 페이지
@app.route('/jonghyuk')
def jonghyuk():
    return render_template('jh/jonghyuk.html')
@app.route('/jonghyuk_music')
def jonghyuk_music():
    return render_template('jh/music.html')
@app.route('/jonghyuk_baber')
def jonghyuk_baber():
    return render_template('jh/baber.html')
@app.route('/jonghyuk_coffee')
def jonghyuk_coffee():
    return render_template('jh/coffee.html')

#선민님 개인 페이지
@app.route('/seonmin')
def seonmin():
    return render_template('sm/seonmin.html')

#재인님 개인 페이지
@app.route('/jaein')
def jaein():
    return render_template('ji/jaein.html')

#나영님 개인 페이지
@app.route('/nayeong')
def nayeong():
    return render_template('ny/nayeong.html')
@app.route('/nayeong_cat')
def nayeong_cat():
    return render_template('ny/cat.html')
@app.route('/nayeong_workout')
def nayeong_workout():
    return render_template('ny/workout.html')
@app.route('/nayeong_travel')
def nayeong_travel():
    return render_template('ny/travel.html')


if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)