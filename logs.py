from flask import Flask
from src.logger import logging
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

    logging.info("We are testing our logging module")

    return "Success Analyticss Project Bootcamp batch"

if __name__ == '__main__':

    app.run(debug=True) # 5000

    # localhost:5000