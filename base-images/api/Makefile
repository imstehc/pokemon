.PHONY:	build
build:
	cp -rf ./../../pokemon/Pipfile Pipfile
	cp -rf ./../../pokemon/Pipfile.lock Pipfile.lock
	cp -rf ./../../pokemon/requirements.txt requirements.txt
	docker build -t registry.gitlab.com/syeriwon/study-projects/pokemon-base:1.0 .
	docker push registry.gitlab.com/syeriwon/study-projects/pokemon-base:1.0
