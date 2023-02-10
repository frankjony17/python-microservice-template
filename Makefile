
# Dependencies Commands
install:
	@poetry lock --no-update
	@poetry install

update:
	@poetry update

# Clean .pyc
clean:
	@echo "Cleaning cache..."
	@find . | egrep '.pyc|.pyo|pycache' | xargs rm -rf
	@find . | egrep '.pyc|.pyo|pycache|pytest_cache' | xargs rm -rf
	@rm -rf ./pycache
	@rm -rf ./.pytest_cache
	@rm -rf ./.mypy_cache
	@echo "Cache cleared!"

# Tool For Style Guide Enforcement
format:
	@echo "Start isort execution:"
	@poetry run isort ./app ./tests
	@echo "Finished isort execution."
	@echo ""

	@echo "Start black execution:"
	@poetry run black ./app ./tests
	@echo "Finished black execution."
	@echo ""

checker:
	@echo "Start flake8 execution:"
	@poetry run flake8 ./app ./tests
	@echo "Finished flake8 execution."
	@echo ""

	@echo "Start pylint execution:"
	@poetry run pylint ./app/
	@echo "Finished pylint execution."
	@echo ""

	@echo "Start mypy execution:"
	@poetry run mypy ./app/
	@echo "Finished pylint execution."
	@echo ""

	@echo "Start bandit execution:"
	@poetry run bandit -v -r ./app/ -c "pyproject.toml"
	@echo "Finished bandit execution."
	@echo ""

# Run app local
run:
	@poetry run uvicorn app.main:application --port 8000 --workers 3 --reload

# Dev tools
localdb:
	@docker run --name basic-postgres --rm -e POSTGRES_USER=app_local_dev -e POSTGRES_PASSWORD=app_local_dev -p 5432:5432 -it postgres:14.1-alpine

docker-build:
	@docker build -t application .

docker-run:
	@docker run -it application -p 8000:8000

# Tests Commands
test:
	@poetry run pytest --cov

test-report:
	@poetry run pytest --cov-report html --cov


# Migrations
migrations:
	@poetry run alembic upgrade heads