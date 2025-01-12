from flask import Flask, render_template, request, redirect
# This is for deploying flask

app = Flask(__name__)

@app.route('/')
def index():
    print('In index')
    return render_template('index.html')

@app.route('/about')
def about():
    print('In about')
    return render_template('about.html')

if __name__ == '__main__':
    app.run(port=33507)
