from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
  myvalue = 'Yo bro'
  myresult = 10 + 20
  return render_template('index.html', myresult=myresult, myvalue=myvalue)

@app.route('/greet/<name>')
def nam(name):
  return f"Hello {name}"

if __name__ == "__main__":
  app.run(host='0.0.0.0', port='3000', debug=True)