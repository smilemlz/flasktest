#使用模板的flask
from flask import Flask,request,render_template

app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def home():
	return render_template('home.html')

@app.route('/signin',methods=['GET'])
def signin_form():
	return render_template('form.html')


@app.route('/signin',methods=['POST'])
def signin():
	if request.form['username'] == 'admin' and request.form['password'] == 'admin':
		return render_template('sign.html',username='admin')
	return render_template('form.html',message='bad username or password')

if __name__ == '__main__':
	app.run()







