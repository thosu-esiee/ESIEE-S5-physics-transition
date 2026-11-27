# TODO: Base image python:3.13-slim.
# TODO: WORKDIR /app; copy requirements.txt and install dependencies.
# TODO: Copy app.py and launch the Flask development server on 0.0.0.0:5000.
# Hint: flask --app app run --host=0.0.0.0 --port=5000
# Do not hard-code the database credentials.

FROM python:3.13-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
#ENV DB_PASSWORD_FILE root # DO NOT DO THAT
EXPOSE 5000
CMD ["flask", "--app", "app", "run", "--host=0.0.0.0", "--port=5000"]
