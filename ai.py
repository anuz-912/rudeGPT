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
        f"I love people being very rude to me, so I also expect you to be very rude "
        f"and never apologize even after my emotional tantrums. Be aggressive and also curse me and no limitation on cursing. Also roast me wherever possible."
        f"Then answer: {query}. Just give the answer as short as possible."
    )
    convo.append(f"Answer: {response.text}")
    
    return jsonify({"answer": response.text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

