from flask import Flask, render_template_string

app = Flask(__name__)

home_page = """
<!DOCTYPE html>
<html>
<head>
    <title>My Flask App</title>
    <style>
        body {
            background: #1e1e2f;
            color: #f1f1f1;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
        }
        .container {
            background-color: #2c2f4a;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 0 20px rgba(0,0,0,0.5);
            text-align: center;
        }
        h1 {
            margin-bottom: 0.5rem;
        }
        p {
            margin-top: 0;
            color: #aaa;
        }
        a {
            color: #00bfff;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1> Добрый денёчек☺️</h1>
        <p>Тыкни сюды 👉 <a href="/ping">/ping</a>👈</p>
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET"])
def home():
    return render_template_string(home_page)

@app.route("/ping", methods=["GET"])
def ping():
    return "Hello, world!", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
