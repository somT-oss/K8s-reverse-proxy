from flask import Flask, jsonify 

app = Flask(__name__)

@app.get("/flask-home")
def flask_home():
    return jsonify({"message": "This is the flask home"}), 200 

@app.get("/nginx-route")
def nginx_route():
    return jsonify({"message": "This is from nginx itself"}), 200

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)