FROM python:3.7-alpine

# update package manager
RUN apk update

# install 3rd party components
RUN apk --no-cache --virtual add build-base 

# update pip
RUN pip install --upgrade pip

# copy and install requirements
COPY ./requirements.txt /usr/src

RUN pip install -r /usr/src/requirements.txt

COPY ./src /usr/src/src

WORKDIR /usr/src/src/

CMD [ "python", "main.py"]

