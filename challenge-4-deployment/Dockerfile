FROM python:3.12-slim

WORKDIR /app

COPY server.py .

ENV PORT=8000

EXPOSE 8000

HEALTHCHECK --interval=5s --timeout=2s --retries=10 CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8000/health', timeout=1)"

CMD ["python", "server.py"]