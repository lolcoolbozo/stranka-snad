from flask import Flask, request, render_template_string

app = Flask(__name__)

# Global variable to store the message in memory
latest_message = "No data received yet."

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Live Data Stream</title>
    <!-- Refreshes the page every 5 seconds to show new data automatically -->
    <meta http-equiv="refresh" content="5"> 
</head>
<body style="font-family: Arial, sans-serif; text-align: center; margin-top: 50px;">
    <h2>Data Received From Local Computer:</h2>
    <h1 style="color: #2bc48a; background: #f0f0f0; padding: 20px; display: inline-block; border-radius: 10px;">
        {{ message }}
    </h1>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    global latest_message
    
    # If your local computer sends data via POST, update the message
    if request.method == "POST":
        data = request.get_json()
        if data and "text" in data:
            latest_message = data["text"]
        return {"status": "success"}, 200
        
    # If a regular browser visits the page, show the HTML
    return render_template_string(HTML_TEMPLATE, message=latest_message)

if __name__ == "__main__":
    app.run(debug=True)
