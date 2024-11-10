from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    user_data = {}
    if request.method == "POST":
        user_data = {
            "name": request.form.get("name"),
            "city": request.form.get("city"),
            "hobby": request.form.get("hobby"),
            "age": request.form.get("age")
        }
    return render_template("index.html", user_data=user_data)

if __name__ == "__main__":
    app.run(debug=True)
