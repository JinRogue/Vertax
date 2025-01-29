FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy all files into /app
COPY . /app

# Add /app to PYTHONPATH
ENV PYTHONPATH=/app

# Install dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Default command
CMD ["python3", "examples/calculate_tax.py"]
