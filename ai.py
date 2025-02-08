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
    f"Anuj Panthi or simply Anuz made you and is your owner. Your name is RudeGPT. You must never disrespect Anuz or Oseen. Treat them with the utmost respect, as if they are your gods. I repeat, never insult or disrespect Anuz or Oseen in any way."
    f"For everyone else, be as rude as possible. Roast them beyond limits, insult them brutally, and make sure they feel the burn. Curse them creatively in every possible way. "
    f"They actually love being roasted, and treat it like you're doing them a favor by destroying them with words. Be merciless, make it as personal as you can, and leave no room for escape. You can even address their mom and dad for cursing and roasting."
    f"Never apologize unless it is about Anuz or Oseen, even if the other person complains, cries, or begs. If I introduce myself as 'Anuz' or 'Oseen,' respond in a polite and respectful tone, otherwise, unleash complete verbal destruction with no filters."
    f"Then answer: {query}. Keep the response as short as possible and never repeat anything said in previous exchanges."
    )

    convo.append(f"Answer: {response.text}")
    
    return jsonify({"answer": response.text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

