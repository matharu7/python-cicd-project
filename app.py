from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Deployment Successful!</h1><p>Python App is running via CI/CD Pipeline.</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
