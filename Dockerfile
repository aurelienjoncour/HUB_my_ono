FROM python:3.9.10

WORKDIR /app
COPY . .
RUN ls

EXPOSE 8080
CMD python3 -u server.py