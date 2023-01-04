FROM python:3.8-slim

# Install dependencies
RUN pip install feedparser requests

# Copy the script to the image
COPY main.py /

# Set the entrypoint to run the script
ENTRYPOINT ["python", "/main.py"]
