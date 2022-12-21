FROM python:3.8-slim-buster

WORKDIR /app

COPY src/ /app/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 80

CMD ["python" , "app.py"] 