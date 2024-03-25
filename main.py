import os.path

from qrcodegenerator import create_qr_code_image
from config import Config

from flask import Flask, send_file, request

app = Flask(__name__)


@app.route("/", methods=['GET'])
def index_get():
    # qr_code_url = url_for('static', filename=CONFIG.QR_CODE_DEFAULT_FILE_NAME)
    form = '<h1>Make a QR code IS218</h1>" <form method="POST" action="/"> \
           <label for="qurl"> QR: URL:</label><br>" \
           <input type="text" id="qurl" name="qurl" value='" + Config.QR_CODE_DEFAULT_URL + "'><br>" \
                "<input type="submit" value="Submit">" \
                "</form>'

    return form

@app.route("/", methods=['POST'])
def index_post():
    full_path  = os.getcwd()
    qr_url = request.form.get("qrurl")
