from flask import Flask, redirect, render_template
import random
app = Flask(__name__)


@app.route("/")
def main():
    return redirect("https://gamaverse.ru/c/frajdej-najt-fankin-fnf-zvezdnyj-chas-protiv-cj-game/")


@app.route("/main")
def main1main():
    return render_template('index.html')


@app.route("/ya")
def main2main():
    rand = random.randint(0, 1)
    if rand == 0:
        return redirect("https://www.google.com/")
    if rand == 1:
        return redirect("https://yandex.ru/")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)
