FROM python:3.8-slim-buster

RUN pip install --upgrade pip

# Copying all files to Source Dir
COPY . /src

# Set workiong dir to the above souyrec dir
WORKDIR /src

# GIve executable permissions
RUN chmod +x docker_train.py

RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]

CMD [ "docer_train.py" ]