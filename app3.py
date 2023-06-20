import pyttsx3
from flask import Flask, render_template, request
from rasa.core.agent import Agent
import asyncio

app = Flask(__name__)
model_path = r"C:\Users\DHARAVATH RAMDAS\hbot22\models\20230620-145401-grizzled-parakeet.tar.gz"  # Replace with the path to your trained Rasa model

# Create the Rasa agent
agent = Agent.load(model_path)

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    sweet_female_voice = None
    for voice in voices:
        if 'f' in voice.name.lower() and 'female' in voice.name.lower():
            sweet_female_voice = voice.id
            break
    if sweet_female_voice:
        engine.setProperty('voice', sweet_female_voice)
    engine.say(text)
    engine.runAndWait()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.form['user_input']

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    response = loop.run_until_complete(agent.handle_text(user_message))

    bot_response = response[0]['text'] if response else "Sorry, I couldn't understand your message."

    speak(bot_response)
    return bot_response

if __name__ == '__main__':
    app.run(debug=True)
