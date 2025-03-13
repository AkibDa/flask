from flask import Flask, render_template, session

app = Flask(__name__, template_folder='templates')
app.secret_key = 'SOME KEY'

@app.route('/')
def index():
  return render_template('two.html', message='Index')

@app.route('/set_data')
def set_data():
  session['name'] = 'Akib'
  session['other'] = 'Yo Bro'
  return render_template('two.html', message='set_data')

@app.route('/get_data')
def get_data():
  if 'name' in session.keys() and 'other' in session.keys():
    name = session['name']
    other = session['other']
    return render_template('two.html', message=f'Name: {name}, Other: {other}')
  else:
    return render_template('two.html', message='No session found')
  
@app.route('/clear_session')
def clear_session():
  session.clear()
  return render_template('two.html', message='Session cleared')
  

if __name__ == '__main__':
  app.run(host='0.0.0.0', port='3000', debug=True)