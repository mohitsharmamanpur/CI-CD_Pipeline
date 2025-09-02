FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy Python app
COPY app.py /app/app.py

# Install Flask
RUN pip install flask

# Expose port
EXPOSE 5000

# Run Flask app
CMD ["python", "app.py"]
