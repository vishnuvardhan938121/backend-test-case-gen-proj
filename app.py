from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/')
def home():
    return "Welcome to the home page"

@app.route('/generate/test-cases', methods=['POST'])
def generate_test_cases():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid request, no JSON payload provided"}), 400
        
        code = data.get('code', '').strip()
        algorithm = data.get('algorithm_name', '').strip()
        language = data.get('language', '').strip()

        if not code or not algorithm or not language:
            return jsonify({"error": "Missing required fields: code, algorithm_name, or language"}), 400

        # Generate dummy test cases (replace this with your logic)
        test_cases = []
        for i in range(1, 6):  # Example: Generate 5 test cases
            input_array = random.sample(range(1, 100), random.randint(5, 10))
            expected_output = sorted(input_array)  # Example for sorting algorithms
            test_cases.append({
                "input": input_array,
                "expected_output": expected_output
            })

        return jsonify({"test_cases": test_cases})

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


if __name__ == '__main__':
    app.run(debug=True)
