
start:
	docker compose up -d

stop:
	docker compose down

restart:
	docker compose down
	docker compose up -d

build:
	docker compose build

logs:
	docker compose logs inference-server -f