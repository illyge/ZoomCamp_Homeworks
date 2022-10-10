import pickle

def exec():
    with open('dv.bin', 'rb') as f_in:
        dv = pickle.load(f_in)
    with open('model1.bin', 'rb') as f_in:
        model = pickle.load(f_in)
    client = {"reports": 0, "share": 0.001694, "expenditure": 0.12, "owner": "yes"}
    client_dv = dv.transform(client)
    proba = model.predict_proba(client_dv)
    print(proba[0][1])


if __name__ == '__main__':
    exec()

