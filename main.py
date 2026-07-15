from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>My Fancy App</title>
        <style>
            body {
                background: linear-gradient(135deg, #667eea, #764ba2);
                color: white;
                text-align: center;
                font-family: Arial;
                margin-top: 100px;
            }
            h1 {
                font-size: 50px;
            }
            p {
                font-size: 20px;
            }
            button {
                padding: 10px 20px;
                background: #ff9800;
                border: none;
                color: white;
                font-size: 18px;
                border-radius: 5px;
            }
        </style>
    </head>
    <body>
        <h1>🚀 Welcome Dear Students!</h1>
        <p>Your App Engine app is live on GCP 🎉</p>
        <button onclick="alert('Hello from GCP!')">Click Me</button>
    </body>
    </html>
    """
if __name__ == "__main__":
    app.run()
