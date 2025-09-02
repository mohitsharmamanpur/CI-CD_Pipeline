FROM redhat/ubi8

# Set working directory
WORKDIR /app

# Copy all files into the container
COPY . /app

# Install Python 3 and pip
RUN yum install -y python3 python3-pip && \
    pip3 install --no-cache-dir flask

# Expose port
EXPOSE 5000

# Run the Flask app
CMD ["python3", "app.py"]
