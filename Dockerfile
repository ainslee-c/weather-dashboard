FROM python:3.11-slim  # Using a more recent version

WORKDIR /app

COPY . .

RUN pip install flask requests python-dotenv

EXPOSE 5002  # Update this to match your new port

CMD ["python", "app.py"]