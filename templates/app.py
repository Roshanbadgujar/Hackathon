from flask import Flask, render_template, request

app = Flask(__name__)

# Map user-friendly names to HTML file paths
PAGES = {
    "newtons_first_low": "newton_first.html",
    "newtons_second_low": "newton_second.html",
    "newtons_third_low": "newton_third.html",
}


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/search', methods=['POST'])
def search_page():
    page_name = request.form.get('page_name', '').lower().replace(" ", "_")
    if page_name in PAGES:
        return render_template(PAGES[page_name])
    else:
        return render_template("error.html", message=f"Page '{page_name}' not found!")

if __name__ == '__main__':
    app.run(debug=True)
