from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.form['user_input']
    response = requests.post('http://localhost:5005', json={"message": user_message})
    parsed_response = json.loads(response.text)
    print(parsed_response)  # Add this line to print the parsed response
    bot_response = parsed_response[0]['text']
    return bot_response


if __name__ == '__main__':
    app.run(debug=True)
