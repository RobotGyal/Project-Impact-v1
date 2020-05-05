# Pull Python image 
FROM python:3

# Set working directory to 'container' folder
WORKDIR /container

# Move the requirements file into the working directory
COPY requirements.txt ./

# 
RUN pip3 install -r requirements.txt

# 
COPY . .

# 
RUN python3 docker_complete.py