from flask_app import app # Don't forget this line!
# HIGHLY RECOMMENDED THAT YOU CREATE YOUR CONTROLLER FILES THAT YOU'LL NEED, THEN IMPORT THEM HERE IMMEDIATELY!
from flask_app.controllers import players, teams # For each controller, import each file here!

if __name__ == "__main__":
    app.run(debug=True)