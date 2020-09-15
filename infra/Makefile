.PHONY:	build-api
build-api:
	cd ../pokemon/ && docker build -t registry.gitlab.com/syeriwon/study-projects/pokemon:1.0 .
	docker push registry.gitlab.com/syeriwon/study-projects/pokemon:1.0

.PHONY: create-network-docker
create-network-docker:
	docker network create pokemon_infra

.PHONY: remove-api
remove-api:
	docker rm -f api

.PHONY: remove-db
remove-db:
	docker rm -f db

.PHONY: remove-image
remove-image:
	docker rmi registry.gitlab.com/syeriwon/study-projects/pokemon:1.0

.PHONY: deploy-api
deploy:
	docker-compose --file docker-compose.yml pull api
	docker-compose up -d

