# Use lightweight Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir fastapi uvicorn openai pydantic

# Expose port
EXPOSE 7860

# Run server
CMD ["uvicorn", "server.app:app", "--host", "0.0.0.0", "--port", "7860"]