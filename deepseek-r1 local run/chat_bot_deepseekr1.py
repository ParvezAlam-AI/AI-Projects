import ollama

def chat_deepseekr1(prompt):
    response = ollama.chat(model="deepseek-r1:7b", messages=[{"role": "user", "content": prompt}])
    return response["message"]["content"]

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        response = chat_deepseekr1(user_input)
        print("AI:", response)

