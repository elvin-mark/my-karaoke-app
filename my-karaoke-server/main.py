from flask import Flask, request
from flask_cors import CORS
from karaoke import Karaoke

app = Flask(__name__)
CORS(app)
core = Karaoke()

@app.route("/")
def home():
    return "Welcom to My Karaoke"

@app.route("/api/songs",methods=["GET"])
def list_songs():
    return core.get_songs()

@app.route("/api/upload",methods=["POST"])
def new_song():
    return core.add_new_song(None)

@app.route("/api/song/{id}",methods=["GET"])
def get_song(song_id:int):
    return core.get_song(song_id)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)