from flask import Flask, request, jsonify
from flask_cors import CORS
from testgenerator import generate_test_cases  # Import the generate_test_cases function

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/')
def home():
    return "Welcome to the home page"

@app.route('/generate/test-cases', methods=['POST'])
def generate_test_cases_route():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid request, no JSON payload provided"}), 400
        
        algorithm = data.get('algorithm_name', '').strip()

        if not algorithm:
            return jsonify({"error": "Missing required field: algorithm_name"}), 400

        # Use the generate_test_cases function from testgenerator.py
        test_cases = generate_test_cases(algo_type="sorting", algo_name=algorithm)

        return jsonify({"test_cases": test_cases})

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


if __name__ == '__main__':
    app.run(debug=True)
