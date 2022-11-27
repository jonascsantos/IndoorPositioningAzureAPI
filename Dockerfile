FROM python:3.9

WORKDIR /fastapi-app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt 

RUN pip install scikit-learn micromlgen firebase_admin PythonSed pyserial python-dateutil

RUN curl -fsSL https://raw.githubusercontent.com/arduino/arduino-cli/master/install.sh | sh
RUN wget https://github.com/mikefarah/yq/releases/latest/download/yq_linux_amd64 -O /usr/bin/yq &&\
    chmod +x /usr/bin/yq
RUN bin/arduino-cli config init

RUN yq -i '.board_manager.additional_urls = ["https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json"]' ~/.arduino15/arduino-cli.yaml 
RUN yq -i '.library.enable_unsafe_install = true' ~/.arduino15/arduino-cli.yaml 

RUN ./bin/arduino-cli core update-index
RUN ./bin/arduino-cli core install esp32:esp32
RUN ./bin/arduino-cli lib install --git-url https://github.com/tzapu/WiFiManager.git https://github.com/mobizt/Firebase-ESP32.git

COPY ./main.py ./app/main.py
COPY ./classifierGenerator.py ./app/classifierGenerator.py
COPY ./featureVectorConverter.py ./app/featureVectorConverter.py

EXPOSE 80

CMD ["python", "./app/main.py"]