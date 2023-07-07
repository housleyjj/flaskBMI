FROM python:3.12.0b3-alpine

WORKDIR /app

RUN pip3 install flask

COPY . . 

CMD [ "python", "-m", "flask", "run", "--host=0.0.0.0", "--debug" ]