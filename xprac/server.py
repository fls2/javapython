from flask import Flask, render_template, request
import wi

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    등급 = '데이터를 넣으세요.'
    if request.method=='POST':
        esti = wi.getModel()
        a = request.form['a']
        b = request.form['b']
        c = request.form['c']
        d = request.form['d']
        e = request.form['e']
        f = request.form['f']
        g = request.form['g']
        h = request.form['h']
        i = request.form['i']
        j = request.form['j']
        k = request.form['k']
        l = request.form['l']
        등급 = esti.predict([[a,b,c,d,e,f,g,h,i,j,k,l]])
        if 등급[0] == 1:
            등급 = '상위입니다.'
        else:
            등급 = '하위입니다.'
    return render_template("index.html",등급=등급)
app.run(debug=True)

       