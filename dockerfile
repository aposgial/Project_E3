FROM  python:3.10

EXPOSE 8000

WORKDIR /

COPY happy_traveller .

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .