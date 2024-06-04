from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    # index.htmlをレンダリング
    return render_template("index.html")

# POSTメソッドでアクセスされた場合の処理
@app.route("/", methods=["POST"])
def result():
    # 何も選択されていない場合はindex.htmlをレンダリング
    if "choice" not in request.form:
        return render_template("index.html")

    # POSTされた値を取得
    user = request.form["choice"]
    # コンピューターのじゃんけんの手をrock,paper,scissorsの中からランダムで選択
    computer = random.choice(["rock", "paper", "scissors"])
    # 勝敗を判定
    if user == computer:
        result = "Draw"
    elif user == "rock" and computer == "scissors":
        result = "Win"
    elif user == "paper" and computer == "rock":
        result = "Win"
    elif user == "scissors" and computer == "paper":
        result = "Win"
    else:
        result = "Lose"
    return render_template("index.html", user=user, computer=computer, result=result)

if __name__ == "__main__":
    app.run(debug=True)