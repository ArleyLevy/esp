from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Estado inicial dos LEDs (todos desligados)
led_status = {
    "led1": False,
    "led2": False,
    "led3": False,
    "led4": False
}

# Rota principal para carregar a página HTML
@app.route('/')
def index():
    return render_template('index.html')

# Rota para atualizar o status dos LEDs
@app.route('/update_led', methods=['POST'])
def update_led():
    global led_status
    data = request.get_json()
    # Atualiza o estado dos LEDs com base no JSON recebido do ESP
    led_status.update(data)
    return jsonify({"status": "OK"}), 200

# Rota para obter o status dos LEDs
@app.route('/led_status', methods=['GET'])
def get_led_status():
    return jsonify(led_status)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
