import pymysql
from flask import Flask, render_template, request, redirect, url_for
from sklearn.linear_model import LinearRegression
import uuid

app = Flask(__name__, static_folder='./flask/static/',
            template_folder='./flask/templates/')

lr = LinearRegression()
lr.fit([[1], [2], [3]], [3, 4, 5])


db = pymysql.connect(host="localhost", user="root",
                     passwd="1234", db="free_board", charset="utf8")
cur = db.cursor()

# cur.execute('DROP TABLE IF EXISTS aaa')
# cur.execute(''' CREATE TABLE `aaa` (
#   `aa` varchar(45) NOT NULL,
#   `bb` varchar(45) DEFAULT NULL,
#   `filename` varchar(100) DEFAULT NULL,
#   `filename_uuid` varchar(100) DEFAULT NULL
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3''')

# 일반적인 라우트 방식입니다.


@app.route('/board/insert')
def insert():
    return render_template("board/insert.html")


@app.route('/board/insertproc', methods=['POST'])
def insertproc():
    print(request.args)
    aa = request.form['aa']
    bb = request.args.get('bb')
    f = request.files['file']
    #  path = os.path.join(app.config['UPLOAD_DIR'], fname)
    #     f.save(path)
    myuuid = f'{uuid.uuid1()}.{f.filename.split(".")[1]}'
    f.save(myuuid)
    try:
        cur.execute(
            f"insert into aaa values ('{aa}','{bb}','{f.filename}','{myuuid}')")
        db.commit()
    except Exception as e:
        print(e)
    print('잘됨')
    return redirect("/board/index")

# 파일 다운로드 처리


@app.route('/fileDown', methods=['GET', 'POST'])
def down_file():
    if request.method == 'POST':
        sw = 0
        files = os.listdir("./uploads")
        for x in files:
            if(x == request.form['file']):
                sw = 1

        path = "./uploads/"
        return send_file(path + request.form['file'],
                         attachment_filename=request.form['file'],
                         as_attachment=True)


@ app.route('/board/index')
def boardindex():
    # select_stmt = "SELECT * FROM aaa WHERE emp_no = %(emp_no)s"
    # cur.execute(select_stmt, { 'emp_no': 2 })
    sql = "select * FROM aaa"
    cur.execute(sql)
    rs = cur.fetchall()
    return render_template("board/index.html", list=rs)


@ app.route('/board')
def board():
    return "그냥 보드"

# URL 에 매개변수를 받아 진행하는 방식입니다.


@ app.route('/board/<article_idx>')
def board_view(article_idx):
    return article_idx

# 위에 있는것이 Endpoint 역활을 해줍니다.


@ app.route('/boards', defaults={'page': 'index'})
@ app.route('/boards/<page>')
def boards(page):
    return page+"페이지입니다."


@ app.route('/')
def index():
    return render_template('index.html')


@ app.route('/predict/<int:predictx>')
def predict(predictx):
    predicty = lr.predict([[predictx]])
    return render_template('index.html', predicty=predicty)


app.run(host="localhost", port=5001, debug=True)
