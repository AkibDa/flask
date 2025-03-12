from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  return "Hello World"

@app.route('/greet/<name>')
def nam(name):
  return f"Hello {name}"

if __name__ == "__main__":
  app.run(host='0.0.0.0', port='3000', debug=True)