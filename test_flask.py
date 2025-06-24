from flask import Flask, request

app = Flask(__name__)

@app.route('/testjson', methods=['POST'])
def testjson():
    print("Request object:", type(request))
    data = request.get_json(force=True)
    print("Data:", data)
    return {"status": "ok"}

if __name__ == '__main__':
    app.run(debug=True)
