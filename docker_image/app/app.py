from flask import Flask
app = Flask(__name__)

@app.route("/")
def def1 ():
  return 'Open a new tab and enter /Welcome/name for URL'

@app.route('/Welcome/<name>')
def Welcome_name(name):
  return 'Welcome and go testing dude!! ' + name + '!'

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)