from flask import Flask, render_template, request, jsonify
import pandas as pd
import ml_backend
from flask_socketio import SocketIO, emit
from datetime import datetime


app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/graph')
def graph():
    return render_template('graph.html')

@app.route('/process_json', methods=['POST'])
def process_json():
    try:
        # Get JSON data from the request
        json_data = request.get_json()

        # Check if the required keys are present in the JSON data
        required_keys = {'AB', 'BC', 'BD', 'CF', 'DE'}
        if not all(key in json_data for key in required_keys):
            return jsonify({'error': 'Missing required keys in JSON'}), 400

        # Print the received JSON data
        # print('Received JSON data:', json_data)
        for station_name in json_data:
            data_dict = dict(json_data[station_name])
            df = pd.DataFrame(data_dict,index=[0])
            iv = {"Ia":data_dict["Ia"], "Va":data_dict["Va"]}

            c = datetime.now()
            current_time = c.strftime('%H:%M:%S')

            for msg in ml_backend.analyze_data(station_name,df,current_time):
                socketio.emit('ml_process_update', {'station': station_name, 'messages': msg,'iv':iv})
                

        # You can perform further processing with the JSON data here

        return jsonify({'message': 'JSON data processed successfully'})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
