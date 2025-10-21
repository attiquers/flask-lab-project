from flask import Flask, jsonify, request, render_template

app = Flask(_name_, static_folder='static', template_folder='templates')

@app.route('/')
def home():
    # If template exists, render it; otherwise return simple JSON.
    try:
        return render_template('index.html')
    except Exception:
        return jsonify({
            'message': ' meow to Flask Lab Project',
            'routes': ['/', '/health', '/data']
        })

@app.route('/health')
def health():
    return 'OK', 200

@app.route('/data', methods=['POST'])
def data():
    if not request.is_json:
        return jsonify({'error': 'Request must be JSON'}), 400
    payload = request.get_json()
    return jsonify({'received': payload}), 201

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000, debug=True)