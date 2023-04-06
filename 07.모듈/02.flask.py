from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return '''
        <h1>Hello World</h1>
    '''

@app.route('/chart')
def chart():
    return render_template('chart.html')
@app.route('/clock')
def clock():
    return render_template('clock.html')

if __name__ == '__main__':
    app.run(debug=True)