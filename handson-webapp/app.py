from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    # index.htmlをレンダリング
    return render_template("index.html")

# ここにじゃんけんゲームの処理を記述する



if __name__ == "__main__":
    app.run(debug=True)