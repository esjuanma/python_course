from flask import Flask, render_template, request

app = Flask(__name__)

totalScore = 0

@app.route('/home')
def home():
    global totalScore

    # Gets score argument from URL
    score = request.args.get('score')

    # If argument exists
    if score is not None:
        score = int(score)
        totalScore = totalScore + score

    data = {
        'firstname': 'Jon',
        'lastname': 'Snow',
        'score': totalScore
    }

    # return app.send_static_file('index.html')
    return render_template('index.html', data = data)

if __name__ == "__main__":
    app.run(debug = True)