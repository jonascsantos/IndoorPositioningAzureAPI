FROM python:3.9

WORKDIR /fastapi-app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt 

RUN pip install scikit-learn micromlgen

COPY ./main.py ./app/main.py
COPY ./classifierGenerator.py ./app/classifierGenerator.py
COPY ./featureVectorConverter.py ./app/featureVectorConverter.py

EXPOSE 80

CMD ["python", "./app/main.py"]