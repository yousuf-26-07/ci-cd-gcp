from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/student-details', methods=['GET'])
def get_details():
    data = {
        "name": "Yousuf harris",
        "roll_number": "2023BCS0013"
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)