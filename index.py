# Заготовка для сервера приложения
from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# HTML template for the web app
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Scilog citations application</title>
</head>
<body>
    <h1>Scilog search article</h1>
    <form id="searchForm" onsubmit="sendQuery(); return false;">
        <input type="text" id="query" name="query" placeholder="Enter your search..." oninput="toggleButton()">
        <button type="button" id="searchButton" onclick="sendQuery()" disabled>Search</button>
    </form>
    <div id="result" style="margin-top:20px;"></div>
    <script>
        function toggleButton() {
            const query = document.getElementById('query').value;
            const button = document.getElementById('searchButton');
            button.disabled = query.length < 3;
        }

        async function sendQuery() {
            const query = document.getElementById('query').value;
            if (query.length < 3) return;
            const response = await fetch('/search', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ query: query })
            });
            const data = await response.json();
            document.getElementById('result').innerText = data.message;
        }
    </script>
</body>
</html>
"""


# Route to serve the HTML page
@app.route("/")
def index():
    return render_template_string(HTML_TEMPLATE)


# API route to handle search requests
@app.route("/search", methods=["POST"])
def search():
    data = request.get_json()
    query = data.get("query", "")

    # Simulate a server operation (placeholder)
    response_message = f"You searched for: {query}"

    return jsonify({"message": response_message})


if __name__ == "__main__":
    app.run(debug=True)
