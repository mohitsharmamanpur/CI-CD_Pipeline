FROM redhat/ubi8

# Install Python 3
RUN yum install -y python3 && yum clean all

# Install Flask
RUN pip3 install flask

# Copy Flask app into container
COPY app.ipynb /app.ipynb

# Expose port 5000
EXPOSE 5000

# Run the app
CMD ["python3", "/app.py"]
