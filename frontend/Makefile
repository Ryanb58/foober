
.PHONY: help
help: ## Display callable targets.
	@echo "Reference card for usual actions."
	@echo "Here are available targets:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'


.PHONY: serve
serve: ## Dev Mode
	docker run --rm -t -v $(pwd):/app -w /app -p 8080:8080 node:latest bash -c "npm install && npm run serve"


.PHONY: build
build: ## Build files for prod
	docker run --rm -v $(pwd):/app -w /app node:latest bash -c "npm install && npm run build"
