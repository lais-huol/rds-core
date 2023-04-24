docker build -t rds-framework .
 
docker run -it --rm -v `pwd`:/app rds-framework bash -c 'flake8 --statistics --benchmark --doctests'

docker run -it --rm -v `pwd`:/app rds-framework bash -c 'mypy --warn-unused-configs --python-version 3.10 --show-error-context --show-column-numbers --show-error-end --show-error-codes --pretty rds_framework'