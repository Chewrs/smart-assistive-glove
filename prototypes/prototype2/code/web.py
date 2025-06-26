from flask import Flask, request, render_template_string
import json
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


@app.route('/last', methods=['GET'])
def test():
	last_string = data_log[-1]
	last_list = json.loads(last_string)
	last_number = last_list[-1]
	html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Auto Refresh</title>
        <meta http-equiv="refresh" content="1"> <!-- Refresh every 2 seconds -->
    </head>
    <body>
        <h2>The distance is: <span style="color:blue; font-size:24px;">{{ number }}</span> cm </h2>
    </body>
    </html>
    """
	return render_template_string(html, number=last_number)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

