#EW
#
#Base Ubuntu image
FROM ubuntu:16.04

#Update package and install python3 and pip in order to install the packages
# listed in "requirements.txt"
RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

#Copy requirements.txt from host to build dependency image before the actual 
# application image layer that will likely change frequently
COPY requirements.txt /app/requirements.txt

#Set working directory of container
WORKDIR /app/

#Build dependency image
RUN pip3 install -r requirements.txt

#Copy application files from host after dependency image is generated
COPY . /app/

#Set the entrypoint for the api
ENTRYPOINT ["python3"]

#Runs the api
CMD ["webapp.py"]

