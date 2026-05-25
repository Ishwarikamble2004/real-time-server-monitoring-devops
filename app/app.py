from flask import Flask, render_template
import psutil
import socket
import platform
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent
    hostname = socket.gethostname()
    system = platform.system()
    uptime = datetime.now().strftime("%H:%M:%S")

    return render_template(
        'index.html',
        cpu=cpu,
        memory=memory,
        hostname=hostname,
        system=system,
        uptime=uptime
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)