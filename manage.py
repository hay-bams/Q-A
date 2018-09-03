import os

from config import config
from main import create_app

config_name = os.getenv('FLASK_ENV', default='development')
app = create_app(config[config_name])

@app.route('/')
def hello():
    return 'Hello world'

if __name__ == '__main__':
    app.run()