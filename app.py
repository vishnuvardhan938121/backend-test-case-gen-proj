from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
import random  # Import random module

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
@app.route('/')
def home():
        return "Welcome to the home page"
@app.route('/generate/test-cases', methods=['POST'])
def generate_test_cases():
    data = request.get_json()

    # Example of test case generation based on the code, algorithm, and language
    algorithm = data['algorithm_name']
    
    # Generate dummy test cases for example purposes
    test_cases = []
    for i in range(1, 21):
        # Generate random input array
        input_array = random.sample(range(1, 100), random.randint(5, 10))
        
        # Example dummy expected output: sorting the input array (this should be replaced with actual expected outputs)
        expected_output = sorted(input_array)
        
        test_cases.append({
            'input': input_array,
            'expected_output': expected_output
        })
    
    return jsonify({'test_cases': test_cases})

if __name__ == '__main__':
    app.run(debug=True)
