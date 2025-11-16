
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
	docker compose logs app -f

# "status"
st:
	docker ps

gen_private_key:
	openssl genpkey -algorithm RSA -pkeyopt rsa_keygen_bits:2048 -out private_key.pem

gen_public_key:
	openssl rsa -pubout -in private_key.pem -out public_key.pem