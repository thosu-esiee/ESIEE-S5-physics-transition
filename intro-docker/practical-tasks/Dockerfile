FROM python
# LABEL is useless, I do not want to publish it with my student credentials
WORKDIR /app
COPY program.py /app/program.py
RUN chmod +x /app/program.py
ENTRYPOINT ["python", "/app/program.py"]
