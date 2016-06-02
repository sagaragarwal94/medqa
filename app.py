from flask import Flask
app = Flask(_name_)

@app.route('/')
def index():
	return '<h1>Hello World</h1>'

if _name_ == '__main__':
	app.run(debug=True)