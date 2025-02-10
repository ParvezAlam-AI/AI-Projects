import ollama
import pyttsx3
import re

# Initialize the text-to-speech engine globally.
engine = pyttsx3.init()
engine.setProperty('rate', 150)      # Speed of speech
engine.setProperty('volume', 0.9)      # Volume of speech

def speak(text):
    """Speak the provided text using the global pyttsx3 engine."""
    engine.say(text)
    engine.runAndWait()

def load_prompt():
    """Load the coach's personality from external file."""
    with open('./coach_prompt1.txt', 'r', encoding='utf-8') as f:
        return f.read().strip()

def clean_response(response):
    """Extracts only the final output from the model's response."""
    lines = response.strip().split('\n')
    return lines[-1].strip() if lines else response.strip()

def is_too_positive(response):
    """Checks if the response is too positive or neutral."""
    positive_words = [
        "great", "good", "well done", "amazing", "improved", "win", "better", 
        "success", "proud", "deserve", "appreciate", "fantastic", "congrats", "encourage"
    ]
    return any(word in response.lower() for word in positive_words)

def witty_coach():
    print("Coach Ironjaw - Ruthless Sarcastic Mode (type 'bye' to exit)")
    
    # Load the system prompt from file.
    system_prompt = load_prompt()
    
    # Append strong reinforcement of behavior
    system_prompt += "\nNEVER be positive. ONLY insults, mockery, and sarcasm. Keep it under 10 words."
    
    # Initialize conversation history
    messages = [{'role': 'system', 'content': system_prompt}]
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            farewell = "Be adidas, not abibas!"
            print("Coach Ironjaw:", farewell)
            speak(farewell)
            break

        # Append the user's message.
        messages.append({'role': 'user', 'content': user_input})
        
        # Reinforce the system prompt
        messages[0] = {'role': 'system', 'content': system_prompt}

        # Call the model with strict temperature settings
        response = ollama.chat(
            model='deepseek-r1:1.5b',
            messages=messages,
            options={'temperature': 0.7, 'top_p': 0.9, 'max_tokens': 20}  # Limit verbosity
        )

        raw_output = response['message']['content']
        coach_reply = clean_response(raw_output)

        # Enforce response behavior: retry if too positive
        if is_too_positive(coach_reply):
            print("Filtering too positive response, retrying...")
            continue

        # Print and speak the coach's response.
        print("Coach Ironjaw:", coach_reply)
        speak(coach_reply)

        # Append the coach's reply to the conversation history.
        messages.append({'role': 'assistant', 'content': coach_reply})

if __name__ == '__main__':
    witty_coach()
