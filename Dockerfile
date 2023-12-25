FROM python:3.8

WORKDIR /app

# Install required packages
RUN pip install fastapi uvicorn python-multipart Pillow

# Copy the application code
COPY . .

# Start the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
