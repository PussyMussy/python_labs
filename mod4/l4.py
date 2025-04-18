from flask import Flask
import subprocess
import platform
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/uptime', methods=['GET'])
def get_uptime():
    uptime_output = subprocess.check_output(['uptime', '-s']).decode('utf-8').strip()
    uptime_output = datetime.strptime(uptime_output, "%Y-%m-%d %H:%M:%S")
    td = datetime.now() - uptime_output 
    total_seconds = int(td.total_seconds())
    days, remainder = divmod(total_seconds, 86400) 
    hours, remainder = divmod(remainder, 3600) 
    minutes, seconds = divmod(remainder, 60)
    uptime = f"{days} дней, {hours}:{minutes}:{seconds}"
    return f"Current uptime is {uptime}"

if __name__ == '__main__':
    app.run(debug=True)
