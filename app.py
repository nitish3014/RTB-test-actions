from flask import Flask, render_template_string

app = Flask(__name__)

# Simple one-page landing page yep
LANDING_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Welcome to HireBright</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin: 0;
            padding: 0;
            background-color: #f4f4f9;
            color: #333;
        }
        .container {
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
            background: white;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #2c3e50;
        }
        .logo {
            width: 150px;
            height: auto;
            margin-bottom: 20px;
        }
        .status {
            color: #27ae60;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Welcome to HireBright</h1>
        <p>Your application is successfully deployed on AWS EKS!</p>
        <p>Container Hostname: <span class="status">{{ hostname }}</span></p>
        <p>Visit Counter: <span class="status">{{ counter }}</span></p>
    </div>
</body>
</html>
"""

counter = 0

@app.route('/')
def home():
    global counter
    counter += 1
    import socket
    hostname = socket.gethostname()
    return render_template_string(LANDING_PAGE, hostname=hostname, counter=counter)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
