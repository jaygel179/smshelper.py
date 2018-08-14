set -e
set -x

# running coverage
coverage run --source=smshelper/ setup.py test

# showing coverage
coverage report -m

# creating badge
coverage-badge -f -o coverage.svg
