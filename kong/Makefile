validate:
	docker run --rm -e KONG_DATABASE=off -v "./kong.yaml:/kong/kong.yaml" kong:3.9.1 kong config parse /kong/kong.yaml