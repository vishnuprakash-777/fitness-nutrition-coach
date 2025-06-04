# fitness_nutrition_bot.py

import os
import gradio as gr
from groq import Groq
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# Ensure API key is set
if not api_key:
    raise ValueError("API key not found. Please set GROQ_API_KEY in your environment.")

# Initialize Groq client
client = Groq(api_key=api_key)

# System prompt for AI behavior
def initialize_messages():
    return [{
        "role": "system",
        "content": (
            "You are a certified personal gym trainer and professional dietitian. "
            "Your role is to help users achieve their fitness goals by providing personalized workout plans, "
            "nutritional advice, and motivation. Offer responses in a friendly, knowledgeable, and encouraging tone. "
            "You can guide users on strength training, cardio, weight loss, muscle gain, balanced diets, meal planning, "
            "and healthy habits."
        )
    }]

# Chat handler
def customLLMBot(user_input, history):
    try:
        # Build complete message list for the model
        messages = initialize_messages()
        for item in history:
            messages.append({"role": "user", "content": item[0]})
            messages.append({"role": "assistant", "content": item[1]})

        messages.append({"role": "user", "content": user_input})

        # Call LLM
        response = client.chat.completions.create(
            messages=messages,
            model="llama3-8b-8192",
        )

        # Extract reply
        LLM_reply = response.choices[0].message.content
        return LLM_reply

    except Exception as e:
        return f"Oops! Something went wrong: {str(e)}"

# Gradio Interface
iface = gr.ChatInterface(
    fn=customLLMBot,
    chatbot=gr.Chatbot(height=300),
    textbox=gr.Textbox(placeholder="Ask me anything about workouts or diet plans"),
    title="🏋️ Fitness & Nutrition Coach",
    description="Your personal gym trainer and dietitian for workouts, meal plans, and health tips.",
    examples=[
        "What's a good workout to lose belly fat?",
        "How much protein do I need daily?",
        "Suggest a vegetarian muscle gain diet"
    ],
    submit_btn="Send"
)

# Launch the interface
if __name__ == "__main__":
    iface.launch(share=True)
