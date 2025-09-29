FROM python:3.11-slim

WORKDIR /code

COPY requirements.txt ./requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

CMD ["fastapi", "run", "app/main.py", "--port", "80"]