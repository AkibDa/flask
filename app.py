from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'GET':
    return render_template('index.html')
  elif request.method == 'POST':
    if 'some key' in request.form.keys():
      username = request.form['username']
      password = request.form['password']
    
    if username == '18700124016' and password == 'skakibahammed':
      return "Success"
    else:
      return "Failure"
    
@app.route('/file_upload', methods=['POST'])
def file_upload():
  file = request.files['file']
  
  if file.content_type == 'text/plain':
    return file.read().decode()
  else:
    return "Please give a '.txt' file"

@app.route('/greet/<name>')
def nam(name):
  return f"Hello {name}"

if __name__ == "__main__":
  app.run(host='0.0.0.0', port='3000', debug=True)