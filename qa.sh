echo "STEP: Lint
"
flake8 --statistics --benchmark --doctests --tee

echo "


STEP: Static type check
"
mypy --warn-unused-configs --python-version 3.10 --show-error-context --show-column-numbers --show-error-end --show-error-codes --pretty rds_framework
