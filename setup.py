from setuptools import setup, find_packages

VERSION = '0.1.1'

setup(
  name='ods-mkdocs-theme',
  version=VERSION,
  url='https://github.com/Orange-OpenSource/ods-mkdocs-theme',
  license='MIT',
  description='Orange Design System MkDocs Theme provides a MkDocs theme for Orange.',
  author='Orange',
  author_email='loic.laussel@orange.com',
  packages=find_packages(),
  include_package_data=True,
  install_requires=[
    'mkdocs-material>=9.0.3'
  ],
  python_requires='>=3.7',
  entry_points={
      'mkdocs.themes': [
        'ods-mkdocs-theme = ods_mkdocs_theme',
      ]
  },
  zip_safe=False
)
