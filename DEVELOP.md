# Developer Guide

## Publication

Our PyPI package has been prepared and published following the instructions in [How to Publish an Open-Source Python Package to PyPI](https://realpython.com/pypi-publish-python-package/#publish-your-package-to-pypi).

When the environment is configured, the package can be prepared by running the following command:

```bash
rm -rf dist/*
python setup.py bdist_wheel sdist --formats gztar
```

Then, the package can be uploaded to PyPI by running the following command:

```bash
twine upload dist/*
```
