.DEFAULT_GOAL := help

migrate: flask db migrate

serve: flask run
