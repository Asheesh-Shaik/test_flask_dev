from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome'



if __name__ == '__main__':
    app.run()  # Run the app in debug mode
