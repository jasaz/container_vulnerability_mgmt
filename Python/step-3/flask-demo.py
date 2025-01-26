# Import Flask Module
from flask import Flask

# Create instance of Flask application
app = Flask(__name__)

@app.route("/")
def main():
  return "<p>Hey there!</p>"

if __name__ == '__main__':
  app.run()
