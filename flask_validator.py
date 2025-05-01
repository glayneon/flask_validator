from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/validate', methods=['POST'])
def validate():
    req = request.get_json()
    uid = req["request"]["uid"]
    obj = req["request"]["object"]

    # conditional for the specific label
    labels = obj.get("metadata", {}).get("labels", {})
    if labels.get("env") == "prod":
        # Check if environment is prod
        return jsonify({
            "response": {
                "uid": uid,
                "allowed": False,
                "status": {
                    "message": "Label 'env=prod' is not allowed."
                }
            }
        })
    
    # allow the request
    return jsonify({
        "response": {
            "uid": uid,
            "allowed": True
        }
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=443, ssl_context=('/certs/tls.crt', '/certs/tls.key'))
    # app.run(host='0.0.0.0', port=80)