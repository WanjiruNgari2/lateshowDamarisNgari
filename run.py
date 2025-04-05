from flask import Flask
from app import create_app

app = create_app()

@app.route('/')
def home():
    return "Welcome to the Late Show!"



if __name__ == "__main__":
    app.run(debug=True)
