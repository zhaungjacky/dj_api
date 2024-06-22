runserver:
	python manage.py runserver 0.0.0.0:8000

makemigrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

shell:
	python manage.py shell

docker_start:
	systemctl --user start docker-desktop

docker_stop:
	systemctl --user stop docker-desktop


docker_force_start:
	systemctl --user force-reload docker-desktop

docker_up:
	docker compose up -d

docker_down:
	docker compose down

create_super_user:
	python manage.py createsuperuser
