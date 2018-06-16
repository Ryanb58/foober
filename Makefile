DOCKER = docker
DOCKERCOMPOSE_DEV = docker-compose

.PHONY: help
help: ## Display callable targets.
	@echo "Reference card for usual actions."
	@echo "Here are available targets:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'


.PHONY: run
run: ## Run the built containers
	${DOCKERCOMPOSE_DEV} up


.PHONY: shell
shell: ## Run Django Shell
	${DOCKERCOMPOSE_DEV} run api python manage.py shell_plus


.PHONY: superuser
superuser: ## Create a Super User
	${DOCKERCOMPOSE_DEV} run api python manage.py createsuperuser


.PHONY: migrations
migrations: ## Make migrations.(manage.py makemgirations)
	${DOCKERCOMPOSE_DEV} run api python manage.py makemigrations
	sudo find . -path *migrations/*.py -exec chown ${USER} {} \;


.PHONY: migrationfileperms
migrationfileperms: ## Show migrations and their permissions on the file sys.
	find . -path *migrations/*.py -exec ls -l {} \;


.PHONY: migrate
migrate: ## Make migrations.(manage.py migrate)
	${DOCKERCOMPOSE_DEV} run api python manage.py migrate


.PHONY: build
build: ## Build the containers
	${DOCKERCOMPOSE_DEV} build

.PHONY: lint-backend
lint-backend: ## Run linter
	${DOCKERCOMPOSE_DEV} exec -T api prospector

.PHONY: lint-frontend
lint-frontend: ## Run frontend linter
	${DOCKERCOMPOSE_DEV} exec -T frontend yarn run lint

.PHONY: test-backend
test-backend: ## Run unit tests
	${DOCKERCOMPOSE_DEV} exec -T api pytest

.PHONY: test-frontend
test-frontend: ## Run jest tests
	${DOCKERCOMPOSE_DEV} exec -T frontend yarn run test

.PHONY: stop
stop: ## Stop all containers.
	${DOCKER} stop $(${DOCKER} ps -q)


.PHONY: killall
kill: ## Kill all containers.
	${DOCKER} kill $(${DOCKER} ps -q)


.PHONY: debug
debug: ## Runs a docker service with service ports turned on (for pdb to work).
ifdef SERVICE
		${DOCKERCOMPOSE_DEV} kill $(SERVICE)
		${DOCKERCOMPOSE_DEV} run --service-ports $(SERVICE)
else
		@echo "Please define SERVICE environment/make variable. Example:"
		@echo
		@echo "SERVICE=api make debug"
		@echo
		@echo "-- or --"
		@echo
		@echo "make debug SERVICE=api"
		@echo
endif


.PHONY: logs
logs: ## Tails an docker services logs.
ifdef SERVICE
		${DOCKERCOMPOSE_DEV} logs -f --tail=400 $(SERVICE)
else
		@echo "Please define SERVICE environment/make variable. Example:"
		@echo
		@echo "SERVICE=api make logs"
		@echo
		@echo "-- or --"
		@echo
		@echo "make logs SERVICE=api"
		@echo
endif


.PHONY: exec
exec: ## Execs into running container.
ifdef SERVICE
		${DOCKERCOMPOSE_DEV} exec $(SERVICE) /bin/sh
else
		@echo "Please define SERVICE environment/make variable. Example:"
		@echo
		@echo "SERVICE=api make exec"
		@echo
		@echo "-- or --"
		@echo
		@echo "make exec SERVICE=api"
		@echo
endif


.PHONY: cleanup
cleanup: ## Clean up all data.
	sudo rm -rf /data/app_name/*
