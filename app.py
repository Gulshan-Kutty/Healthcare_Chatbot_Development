from flask import Flask, render_template, request
from rasa.core.agent import Agent

app = Flask(__name__)

# Load the Rasa agent
model_path = "C:\\Users\\91976\\OneDrive\\Desktop\\Chatbot\\RASA_Healthcare\\models"
agent = Agent.load(model_path)

# Define the home route
@app.route('/')
def index():
    return render_template('jst.html')

# Define the chat route
@app.route('/chat', methods=['POST'])
async def chat():
    user_message = request.form['message']
    responses = await agent.handle_text(user_message)
    bot_response = responses[0]['text']
    return bot_response

if __name__ == '__main__':
    app.run(debug=True)
