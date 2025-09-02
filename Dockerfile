FROM redhat/ubi8

# Set working directory
WORKDIR /app

# Install Python & Flask
RUN dnf install -y python3 python3-pip && \
    pip3 install --no-cache-dir flask

# Copy all files
COPY . /app

# Expose Flask port
EXPOSE 5000

# Run Flask app
CMD ["python3", "app.py"]
