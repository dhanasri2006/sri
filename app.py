from flask import Flask, render_template

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/gift')
def gift():
    return render_template('gift.html')

@app.route('/love')
def love():
    return render_template('love.html')

if __name__ == '__main__':
    app.run(debug=True)
