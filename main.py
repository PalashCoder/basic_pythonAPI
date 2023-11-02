from flask import Flask,request,jsonify
app= Flask(__name__)

@app.route("/")
def home():
    return "HOME sdasad"

@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data={
        "User Name": "Palash",
        "User Id": user_id,
    }
    parameter=request.args.get("parameter")
    if parameter:
        user_data["parameter"]=parameter
    return jsonify(user_data), 200

@app.route("/create", methods=["POST"])
def create():
    data =request.get_json()
    return jsonify("New Record Created",data), 200

if __name__ == "__main__":
    app.run(debug=True)