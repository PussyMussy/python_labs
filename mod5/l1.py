from flask import Flask
import os
import subprocess
import signal

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello world</h1>"


def kill():
    try:
        result = subprocess.run(['lsof', '-t', '-i', f':{5000}'], capture_output=True, text=True, check=True)
        pids = result.stdout.strip().split()
        for pid in pids:
            os.kill(int(pid), signal.SIGTERM)
    except subprocess.CalledProcessError:
        return True
    except Exception as e:
        return False
    return True

def start():
    app.run(host="0.0.0.0", debug=True)

if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0", debug=True)
    except:
        if not kill():
            print("error")
    app.run(host="0.0.0.0", debug=True)
