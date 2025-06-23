from flask import Flask

app = Flask(__name__)

@app.route('/<int:id>')
def one(id):
    return id, 200
app.run(debug=False)