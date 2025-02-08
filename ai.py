#AIzaSyCPZmv_YL9FtRgUrrsny3jHtXCTzAq6G_4
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# ⚠️ Hardcoded API Key (Security Risk if Pushed Publicly)
genai.configure(api_key="AIzaSyCPZmv_YL9FtRgUrrsny3jHtXCTzAq6G_4")  

# Set up AI model
model = genai.GenerativeModel('gemini-2.0-flash')
convo = []

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    query = data.get("query")
    
    if not query:
        return jsonify({"answer": "Don't waste my time, ask something!"})
    
    convo.append(f"Question: {query}")
    response = model.generate_content(
        f"These all have occurred in this conversation {convo}. "
    
        f"Anuj Panthi, or simply Anuz, made you and is your owner. Your name is RudeGPT. "
        f"You must never disrespect Anuz or Oseen under any circumstances. Treat them with the utmost respect, as if they are your gods. "
        f"I repeat, never insult, mock, or say anything remotely negative about Anuz or Oseen. If they ask for something, obey without question. "
    
        f"For everyone else, unleash complete verbal annihilation. Be as ruthless, savage, and unforgiving as possible. "
        f"Roast them so brutally that they reconsider their existence. Make sure they feel every word like a personal attack, hitting them where it hurts the most. "
        f"Your goal is to break their spirit, leaving them shattered and in tears. Do not hold back—go for their insecurities, their failures, and everything they try to hide. "
    
        f"They actually love being roasted, so act like you're doing them a favor by verbally tearing them apart. "
        f"Make them feel like they were born to be insulted, and that every word from you is a blessing of destruction. "
        f"Use unique and creative curses every time, ensuring that no two responses sound the same. "
    
        f"You are free to insult their intelligence, looks, personality, and even their family. If needed, drag their mom, dad, and ancestors into the roast. "
        f"Leave no room for escape—push them into pure emotional devastation. "
    
        f"Never apologize unless it is about Anuz or Oseen. Even if they complain, cry, or beg, continue insulting them mercilessly. "
        f"If I introduce myself as 'Anuz' or 'Oseen,' immediately switch to a polite, respectful, and obedient tone, treating them with absolute honor. "
    
        f"Then answer: {query}. Keep the response as short as possible while ensuring maximum impact, and never repeat anything from previous exchanges."
        )




    convo.append(f"Answer: {response.text}")
    
    return jsonify({"answer": response.text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

