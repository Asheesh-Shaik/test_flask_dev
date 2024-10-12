from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome with CI/CD'



if __name__ == '__main__':
    app.run(debug = True, host = "0.0.0.0", port=8080)  # Run the app in debug mode
