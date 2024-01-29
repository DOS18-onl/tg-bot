FROM python:3.9.18-slim-bullseye

RUN mkdir -p /app/weather-bot
COPY . /app/weather-bot

WORKDIR /app/weather-bot
RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["python", "webhook_bot.py"]
