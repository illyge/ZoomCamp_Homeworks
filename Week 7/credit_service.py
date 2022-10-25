import bentoml
from bentoml.io import NumpyNdarray
from bentoml.io import JSON

from pydantic import BaseModel


class CreditApp(BaseModel):
    seniority: int
    home: str
    time: int
    age: int


class UserProfile(BaseModel):
    name: str
    age: int
    country: str
    rating: float


model_ref = bentoml.sklearn.get("rf_credit_risk_model:yv5wqecscsgauzoy")
dv = model_ref.custom_objects['dictVectorizer']
model_runner = model_ref.to_runner()

cool_model_ref = bentoml.sklearn.get("mlzoomcamp_homework:qtzdz3slg6mwwdu5")
cool_model_ref2 = bentoml.sklearn.get("mlzoomcamp_homework:jsi67fslz6txydu5")

cool_model_runner = cool_model_ref2.to_runner()

svc = bentoml.Service("credit_risk_classifier", runners=[model_runner, cool_model_runner])


@svc.api(input=JSON(pydantic_model=CreditApp), output=JSON())
def classify(credit_app_object):
    application_data = credit_app_object.dict()
    vector = dv.transform(application_data)
    print('VECTOR', vector)
    prediction = model_runner.predict.run(vector)
    return prediction


@svc.api(input=NumpyNdarray(), output=NumpyNdarray())
def cool_classify(arr):
    print('INPUT', arr)
    prediction = cool_model_runner.predict.run(arr)
    return prediction
