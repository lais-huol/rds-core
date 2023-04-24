docker build -t rds-core .
 
docker run -it --rm -v `pwd`:/app rds-core bash -c 'flake8 --statistics --benchmark --doctests'

docker run -it --rm -v `pwd`:/app rds-core bash -c 'mypy --warn-unused-configs --python-version 3.10 --show-error-context --show-column-numbers --show-error-end --show-error-codes --pretty rds_core'