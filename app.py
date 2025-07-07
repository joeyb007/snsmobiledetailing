#The app.py file is defined with the purpose of being ht epace from
# which the flask project is run.

# importing the flask app object so that it can be run within this file
from webapp import app

#Running the app when the file is run via terminal, using debug mode
if __name__ == "__main__":
    app.run(debug=True)