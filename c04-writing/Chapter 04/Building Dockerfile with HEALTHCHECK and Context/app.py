
from flask import Flask

app = Flask(__name__)

@app.route('/')

def AwesomeContainers():
    return 'This is a healthy flask application.'

if __name__ == '__main__':
    app.run(host='0.0.0.0')