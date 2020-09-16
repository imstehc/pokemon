# script to build the docker image to api
# it is necessary to build the image api when the project pokemon is changed
.PHONY:	build-api
build-api:
	cd ../pokemon/ && docker build -t registry.gitlab.com/syeriwon/study-projects/pokemon:1.0 .
	docker push registry.gitlab.com/syeriwon/study-projects/pokemon:1.0

# script to create the network to the containers
.PHONY: create-network-docker
create-network-docker:
	docker network create pokemon_infra

# script to remove container api
.PHONY: remove-api
remove-api:
	docker rm -f api

# script to remove container db
.PHONY: remove-db
remove-db:
	docker rm -f db

# script to remove the docker image of the pokemon
# it is necessary to remove the image api when you have build a new image
.PHONY: remove-image
remove-image:
	docker rmi registry.gitlab.com/syeriwon/study-projects/pokemon:1.0

# script to make the deploy to server
.PHONY: deploy-api
deploy:
	docker-compose --file docker-compose.yml pull api
	docker-compose up -d

