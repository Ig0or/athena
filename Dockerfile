FROM python:3.10-slim

EXPOSE 4001

COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /app
COPY . /app

ENV DATABASE_URL="sqlite:///server.db"

CMD ["gunicorn", "--bind", "0.0.0.0:4001", "athena:app"]