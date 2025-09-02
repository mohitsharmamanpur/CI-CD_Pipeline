FROM redhat/ubi8

# Install Python 3
RUN yum install -y python3

# Install Flask using pip3
RUN pip3 install flask

# Copy app.py into the container
COPY app.ipynb /app.ipynb

# Expose port 5000 for Flask
EXPOSE 5000

# Set the command to run the app
CMD ["python3", "/app.py"]
