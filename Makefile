docker-build:
	docker rmi -f falcon_notications:v1 || true
#	docker rmi -f (docker images -q -f 'dangling=true') || true
	docker-compose down
	docker-compose build
docker: docker-build
	docker-compose up -d
	docker-compose logs -f
