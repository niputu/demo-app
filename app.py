from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def index():
    if random.randint(0, 9) < 2:
        return "Internal Server Error", 500
    return "Hello, World! (from Flask)", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
