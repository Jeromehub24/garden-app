FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY garden_advice.py ./

RUN useradd --create-home appuser && chown -R appuser:appuser /app

USER appuser

CMD ["python", "garden_advice.py"]
