from flask import Flask
import os

app = Flask(__name__,
    static_folder=os.path.abspath('application/view/static'),
    template_folder=os.path.abspath('application/view/templates')
    )
if __name__ == "__main__":
    app.run(debug=True)

from application.controller import home_controller
from application.controller import estado_controller
from application.controller import manutencao_controller