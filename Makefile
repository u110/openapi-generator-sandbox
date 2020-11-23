GENERATOR:=python-flask
target-file:=openapi-generator.yaml

generate:
	docker run --rm \
		-v $(CURDIR):/local \
		openapitools/openapi-generator-cli \
		generate \
				-i /local/$(target-file) \
				-g $(GENERATOR) \
				-o /local/out/$(GENERATOR)
