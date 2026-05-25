from flask import Flask, request, render_template_string
from openai import OpenAI

app = Flask(__name__)

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY")
)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>AI Chatbot - Groq</title>
    <style>
        body { font-family: Arial; max-width: 600px; margin: 50px auto; padding: 20px; background: #f5f5f5; }
        h1 { color: #333; text-align: center; }
        .chat-box { background: white; border-radius: 10px; padding: 20px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        input[type="text"] { width: 70%; padding: 10px; border: 1px solid #ddd; border-radius: 5px; font-size: 16px; }
        button { padding: 10px 20px; background: #007bff; color: white; border: none; border-radius: 5px; cursor: pointer; font-size: 16px; }
        button:hover { background: #0056b3; }
        .response { background: #e9ecef; padding: 15px; border-radius: 5px; margin-top:20px; white-space: pre-wrap; }
        .footer { text-align: center; margin-top: 20px; font-size: 12px; color: #666; }
    </style>
</head>
<body>
    <h1>AI Chatbot (Groq)</h1>
    <div class="chat-box">
        <form method="post">
            <input type="text" name="message" placeholder="Skriv din fraga
har..." required>
            <button type="submit">Skicka</button>
        </form>
        {% if response %}
<div class="response"><strong>Svar:</strong><p>{{ response }}</p>
</div>
        {% endif %}
    </div>
    <div class="footer">Drivs av Groq AI | Gratis och snabb</div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def chat():
    response = None
    if request.method == "POST":
        user_message = request.form["message"]

        try:
            completion = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": user_message}]
            )
            response = completion.choices[0].message.content
        except Exception as e:
            response = f"Fel: {str(e)}"

    return render_template_string(HTML, response=response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
