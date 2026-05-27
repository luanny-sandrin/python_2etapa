from flask import Flask, render_template

webapp = Flask(__name__)

@webapp.route('/')
def index():
    return render_template('index.html')

@webapp.route('/pg1')
def pg1():
    return render_template('pg1.html')

@webapp.route('/pg2')
def pg2():
    return render_template('pg2.html')

@webapp.route('/pg3')
def pg3():
    return render_template('pg3.html')

if __name__ == '__main__':
    webapp.run(debug=True)