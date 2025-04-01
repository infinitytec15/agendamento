up:
	docker-compose up --build

down:
	docker-compose down

migrate:
	docker-compose run backend python manage.py migrate

createsuperuser:
	docker-compose run backend python manage.py createsuperuser
