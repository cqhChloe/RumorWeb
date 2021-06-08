from flask import Flask,render_template,request
import datetime
app = Flask(__name__)

#返回给用户渲染后的网页
@app.route('/')
def index():
    return render_template("Mamba_index.html")

@app.route('/index')
def index2():
    time = datetime.date.today() #普通类型
    name = ["A","B","C"] #列表类型
    point = {"J":"A","V":"B"}#字典类型
    return render_template("index.html",var=time,list=name,point=point)

@app.route('/user/<name>')
def welcome(name):
    return 'Hello %s!'%name

@app.route('/test/register')
def register():
    return render_template("/test/register.html")

#需要接受表单的路由2，需要指定method为Post
@app.route('/result',methods=['POST','GET'])
def result():
    if request.method=='POST':
        result=request.form
        return render_template("/test/result.html",result=result)

if __name__ == '__main__':
    app.run(debug=True)
