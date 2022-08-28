

bootstrap:
	docker run --rm --network=kong-net \
		-e "KONG_DATABASE=postgres" \
		-e "KONG_PG_HOST=kong-database" \
		-e "KONG_PG_PASSWORD=kongpass" \
		kong:2.8.1-alpine kong migrations bootstrap