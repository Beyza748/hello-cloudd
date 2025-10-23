from flak import Flask
ask = Flask(__name__)

@app.route('/')
def home():
  return "Merhaba , Buluttan Selam!"
