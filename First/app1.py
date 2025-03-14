from flask import Flask, render_template, request, Response, send_from_directory, jsonify
import pandas as pd
import os
import uuid

app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/')

@app.route('/')
def index():
  
  if request.method == 'GET':
    return render_template('index.html')
  elif request.method == 'POST':
    if 'some key' in request.form.keys():
      username = request.form['username']
      password = request.form['password']
    
    if username == '18700124016' and password == 'skakibahammed':
      return "Success"
    
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
  
  return response

@app.route('/convert_csv_two', methods=['POST'])
def convert_csv_two():
  file = request.files['file']
  df = pd.read_excel(file)
  if not os.path.exists('downloads'):
    os.makedirs('downloads')
  filename = f'{uuid.uuid4()}.csv'
  df.to_csv(os.path.join('downloads', filename))
  return render_template('download.html', filename=filename)

@app.route('/download/<filename>')
def download(filename):
  return send_from_directory('downloads', filename, download_name='result.csv')

@app.route('/handle_post', methods=['POST'])
def handle_post():
  greeting = request.json['greeting']
  name = request.json['name']
  
  with open('file.txt', 'w') as f:
    f.write(f'{greeting}, {name}')
    
  return jsonify({'message': 'Successfully written!'})

@app.route('/greet/<name>')
def nam(name):
  return f"Hello {name}"

if __name__ == "__main__":
  app.run(host='0.0.0.0', port='3000', debug=True)