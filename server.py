from flask import Flask
from dotenv import dotenv_values
from route.routing import routing

# create the server
app = Flask(__name__)

# register the route
app.register_blueprint(routing)

if __name__ == "__main__":
  app.debug = False
  # run debug mode in development status
  if dotenv_values('.env')['ENV'] == 'development':
    app.debug = True

  app.run()
  