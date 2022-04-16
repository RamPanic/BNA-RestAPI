
# Created by RamPanic

# Third-party imports

from flask import Flask

# Local application/library specific imports

from config import config
from routes.bna import bna

# Initial

app = Flask(__name__)

app.config.from_object(config['dev'])

app.register_blueprint(bna)


if __name__ == '__main__':

    app.run(host=app.config["HOST"], port=app.config["PORT"])
