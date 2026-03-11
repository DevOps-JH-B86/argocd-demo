import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    db_name = os.environ.get('DB_NAME', 'Not Set')
    env_name = os.environ.get('ENV_NAME', 'Not Set')
    return f"""
    <html>
        <body>
            <h1>Environment Info</h1>
            <p><strong>DB_NAME:</strong> {db_name}</p>
            <p><strong>ENV_NAME:</strong> {env_name}</p>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)