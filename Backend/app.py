from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/student-details')
def get_details():
    return jsonify({
        "name": "Yousuf harris",
        "roll_number": "2023BCS0013"
    })

app.run(host='0.0.0.0', port=5000)