from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/events')
def events():
	return render_template('events.html')

@app.route('/my-events')
def my_events():
	return render_template('my_events.html')

@app.route('/news')
def news():
	return render_template('news.html')

if __name__ == '__main__':
	app.run(debug=True)