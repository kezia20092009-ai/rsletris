# Letris Hospital – Simple Flask server
# -------------------------------------------------
# Run:  python app.py
# Then open http://127.0.0.1:5000 in your browser.
# -------------------------------------------------
from flask import Flask, render_template

app = Flask(__name__)

# -----------------------------------------------------------------
# Route: the home page (renders index.html)
# -----------------------------------------------------------------
@app.route("/")
def home():
    """
    Render the HTML page. Flask will automatically look inside the
    `templates` folder for the template name passed to render_template.
    """
    return render_template("main.html")

# -----------------------------------------------------------------
# Main entry point
# -----------------------------------------------------------------
if __name__ == "__main__":
    # Enable debug mode for auto‑reload while developing
    app.run(debug=True, port=5000)