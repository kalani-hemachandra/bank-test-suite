FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir pytest
CMD ["pytest", "tests/", "--disable-warnings", "-v"]
