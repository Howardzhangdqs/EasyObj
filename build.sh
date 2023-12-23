rm -rf ./dist

python versionManager.py
python setup.py check
python setup.py sdist bdist_wheel