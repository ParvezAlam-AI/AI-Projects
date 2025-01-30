🚀 DeepSeek R1 Chatbot (Local AI Model)
A powerful AI chatbot running locally on Windows using DeepSeek R1 (7B) and Ollama.

📌 Features

✅ Runs fully offline (no API calls needed)  
✅ Uses DeepSeek R1 (7B) via Ollama  
✅ Fast & responsive AI chat 
✅ Easy to install on Windows  
✅ Windows, macOS, and Linux support  

📥 Installation Guide  
1️⃣ Install Ollama  
Ollama is required to run DeepSeek R1 locally.  

🟢 Windows (via PowerShell)  

winget install Ollama.Ollama  
Or, download it manually from: Ollama Official Website.  

🔵 macOS (via Homebrew)  
brew install ollama  

🟡 Linux   
curl -fsSL https://ollama.com/install.sh | sh  


📥 **Download & Run DeepSeek R1  **
After installing Ollama, download DeepSeek R1 (7B) using:   

powershell  
ollama pull deepseek-r1:7b  
✅ This will download and install the model locally.  

💻 Running DeepSeek R1 in the Terminal  
Once the model is installed, start chatting:  

powershell  

ollama run deepseek-r1:7b   
💬 This will launch an interactive chat with DeepSeek R1 in your terminal.    

🔄 Start & Stop Ollama Service  
Start Ollama in the Background:  
powershell   
ollama serve start  
💡 Why? This keeps Ollama running so you can use it in Python without restarting it each time.  

Stop Ollama Service:  
powershell  
ollama serve stop  
💡 Why? Stops the Ollama server to free up memory.  

📝 **Running Deepseek-r1 in terminal ** 

ollama serve  
ollama run deepseek-r1:7b  
ollama stop deepseek-r1:7b  
CTRL + d to exit

📝 **Running the Python Chatbot ** 
Once DeepSeek R1 is installed, run the chatbot script:  
powershell  
python deepseek_chat.py  


✅ Example Chat Session:  
You: What is DeepSeek R1?    
AI: DeepSeek R1 is a 7-billion parameter transformer model...  
💡 Type "exit" to stop the chat.


🚀 Happy Chatting!  
🔥 Now you have DeepSeek R1 (7B) running locally—no API, no cloud, just pure AI power! 🔥  
