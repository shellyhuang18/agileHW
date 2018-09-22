
from flask import Flask

app = Flask(__name__)

import socket

from app import routes
if __name__ == '__main__':
    # sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # sock.bind(('localhost',0))
    # port = sock.getsockname()[1]
    # sock.close()
    app.run('localhost', 5000, debug=True)
    
















