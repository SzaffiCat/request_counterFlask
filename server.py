from flask import Flask, render_template, redirect

app = Flask(__name__)

counts = 0

@app.route('/')
def index():
    return render_template('route.html', counter = counts)

@app.route('/request-counter')
def request_count():
    global counts
    counts += 1
    return redirect('/')


if __name__ == '__main__':
    app.run(
        debug=True,
        port=5000
    )