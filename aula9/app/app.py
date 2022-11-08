from flask import Flask, render_template
from livereload import Server

app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
	return render_template('index.html')




server = Server(app.wsgi_app)
server.watch('templates/')
server.serve()