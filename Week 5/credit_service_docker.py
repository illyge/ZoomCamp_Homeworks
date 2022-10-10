import pickle
from flask import Flask, request, jsonify

app = Flask('credit_service')
with open('dv.bin', 'rb') as f_in:
    dv = pickle.load(f_in)
with open('model2.bin', 'rb') as f_in:
    model = pickle.load(f_in)

@app.route('/proba', methods=['POST'])
def proba():
    print ('Received data', request.get_json())
    client_dv = dv.transform(request.get_json())
    proba = model.predict_proba(client_dv)
    return jsonify({'proba': proba[0][1]})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9697)