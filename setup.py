import pathlib
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

# This call to setup() does all the work
setup(
    # appears on pypi
    name="donerkebab",
    version="1.0.1",
    description="A super easy to use Selenium browser api wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ytkimirti/donerkebab",
    author="Yusuf Taha KIMIRTI",
    author_email="yusuftaha9@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    # REQUIRED, the packages you are going to export
    packages=["donerkebab"],
    include_package_data=True,
    # Required libraries
    install_requires=["feedparser", "html2text"],
)