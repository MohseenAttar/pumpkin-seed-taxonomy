# from flask import Flask
# from classification_router import routes

# app = Flask(__name__, template_folder='templates')
# app.register_blueprint(routes)

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask
from router.classification_router import routes


app = Flask(__name__, template_folder='templates')
app.secret_key = 'mysecretkey123'
app.register_blueprint(routes)

if __name__ == '__main__':
    app.run(debug=True)

