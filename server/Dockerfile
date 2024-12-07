FROM python:3.10

WORKDIR /app

COPY requirements-base.txt .
RUN pip install -r requirements-base.txt

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]