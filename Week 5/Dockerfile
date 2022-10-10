FROM svizor/zoomcamp-model:3.9.12-slim
COPY ["credit_service_docker.py", "model1.bin", "dv.bin", "Pipfile", "Pipfile.lock", "./"]
RUN pip install pipenv
RUN pipenv install --system --deploy
EXPOSE 9696
ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "credit_service_docker:app"]