FROM python:3-alpine3.15
WORKDIR /app
COPY . /app
RUN pip install flask
EXPOSE 3000
CMD python ./app.py