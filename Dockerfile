FROM redhat/ubi8

WORKDIR /app

# Install Python 3 and upgrade pip
RUN dnf install -y python3 python3-pip && \
    python3 -m pip install --upgrade pip setuptools wheel && \
    pip3 install --no-cache-dir flask

# Copy all files
COPY . /app

# Expose Flask port
EXPOSE 5006

# Run Flask app
CMD ["python3", "app.py"]
