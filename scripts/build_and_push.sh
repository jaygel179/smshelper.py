set -e
set -x

# building
python setup.py sdist bdist_wheel

# test upload
twine upload dist/*
