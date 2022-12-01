from flask import Flask, render_template, request, json, jsonify, make_response
import urllib.request, json
import os
from flask_bootstrap import Bootstrap5


app = Flask(__name__)
bootstrap = Bootstrap5(app)


@app.route("/")
def movies():
    api_key = os.environ.get("TMDB_API_KEY")
    url = "https://api.themoviedb.org/3/genre/movie/list?api_key={}".format(api_key)
    response = urllib.request.urlopen(url)
    data = response.read()
    jsondata = json.loads(data)

    return render_template ("movie.html",genres=jsondata["genres"],apikey=api_key)

@app.route("/get",methods=["POST"])
def get_movies():
    req = request.get_json()
    url = req['request']
    
    response = urllib.request.urlopen(url)
    data = response.read()
    jsondata = json.loads(data)

    res = make_response(jsonify(jsondata), 200)
    return res




if __name__ == '__main__':
    app.run(debug=True)
