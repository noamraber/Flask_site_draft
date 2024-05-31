from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

ESP32_sys_movement = 0  # Global variable to type of movement

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/update_ESP32_sys_movement', methods=['POST'])
def update_ESP32_sys_movement():
    global ESP32_sys_movement
    ESP32_sys_movement = request.json['type']
    print(ESP32_sys_movement)
    return jsonify(status="success", ESP32_sys_movement=ESP32_sys_movement)

@app.route('/get_ESP32_sys_movement', methods=['GET'])
def get_ESP32_sys_movement():
    global ESP32_sys_movement
    return jsonify(status="success", ESP32_sys_movement=ESP32_sys_movement)

@app.route('/power/<int:number>', methods=['GET'])
def power(number):
    result = number ** 2
    return jsonify(status="success", result=result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
