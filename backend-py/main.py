from flask import Flask

app = Flask(__name__)


@app.route('/COW', methods=['GET'])
def helloWorld():
    return 'GGG'


if __name__ == '__main__':
    app.run(debug=True)
