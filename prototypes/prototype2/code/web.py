from flask import Flask, request

app = Flask(__name__)
data_log = []

@app.route('/data', methods=['POST'])
def receive_data():
    data = request.json
    if data:
        data_log.append(data)
        print(f"Received: {data}")
        return {'status': 'success'}, 200
    return {'error': 'No JSON received'}, 400

@app.route('/data', methods=['GET'])
def get_data():
    return {'data': data_log}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
