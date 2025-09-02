FROM redhat/ubi8

# Set working directory
WORKDIR /app

# Install Python 3, upgrade pip, and install Flask
RUN dnf install -y python3 python3-pip && \
    python3 -m pip install --upgrade pip setuptools wheel && \
    pip3 install --no-cache-dir flask

# Copy all files
COPY . /app

# Expose the same unique port as Flask
EXPOSE 50123

# Run Flask app
CMD ["python3", "app.py"]
