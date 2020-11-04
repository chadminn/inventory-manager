#
# Makefile for inventory-manager project
#

#Build docker images and construct the containers
docker:
	docker build routing -t routing && docker build webapp -t webapp
	docker run -d --name=routing --net=host routing
	docker run -d --name=webapp --net=host webapp


#Locally run routing application
build:
	python3 -m venv venv
	. venv/bin/activate; \
	pip install -r requirements.txt; \

run: 
	. venv/bin/activate; \
	cd routing; \
	python3 routing.py;
