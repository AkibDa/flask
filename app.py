from flask import Flask, render_template, request, Response
import pandas as pd

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
  elif file.content_type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' or file.content_type == 'application/vnd.ms-excel':
    df = pd.read_excel(file)
    return df.to_html()
  
@app.route('/convert_csv', methods=['POST'])
def convert_csv():
  file = request.files['file']
  df = pd.read_excel(file)
  
  response = Response(
    df.to_csv(),
    mimetype='text/csv',
    headers={
      'Content-Disposition': 'attachment; filename=result.csv'
    }
  )
  

@app.route('/greet/<name>')
def nam(name):
  return f"Hello {name}"

if __name__ == "__main__":
  app.run(host='0.0.0.0', port='3000', debug=True)