FROM python:3.13.2-slim
RUN useradd app

USER app
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir --target=./packages -r requirements.txt
env PYTHONPATH=/app/packages

COPY . .

EXPOSE 5000

CMD ["python", "main.py"]
