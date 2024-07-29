# Use the official Kali Linux image as a base
FROM kalilinux/kali-rolling

# Update the package list and install required packages
RUN apt-get update && apt-get install -y \
    python3-pip \
    software-properties-common \
    build-essential \
    cmake \
    libgtk-3-dev \
    libboost-all-dev \
    whatweb \
    host \
    wget \
    wapiti \
    nikto \
    davtest \
    dnsmap \
    nmap

# Install wafw00f using pip
RUN pip3 install wafw00f

# Copy the web_scan.py script to the container
COPY web_scan.py /usr/src/app/web_scan.py

# Copy the Flask application to the container
COPY app /usr/src/app

# Set the working directory
WORKDIR /usr/src/app

# Install Flask
RUN pip3 install Flask

# Expose the port the app runs on
EXPOSE 5000

# Command to run the Flask application
CMD ["python3", "app.py"]
