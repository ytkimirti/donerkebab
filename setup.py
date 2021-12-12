import io
from setuptools import (
    setup,
    find_packages,
)  # pylint: disable=no-name-in-module,import-error


def dependencies(file):
    with open(file) as f:
        return f.read().splitlines()


with io.open("README.md", encoding="utf-8") as infile:
    long_description = infile.read()

setup(
    name="donerkebab",
    packages=find_packages(exclude=("tests", "examples")),
    version="0.0.2",
    license="MIT",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    python_requires=">=3.6",
    description="Super easy to use selenium wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="ytkimirti",
    author_email="yusuftaha9@gmail.com",
    url="https://github.com/ytkimirti/donerkebab",
    keywords=[
        "selenium",
        "wrapper",
        "chrome",
        "firefox",
        "easy",
        "beginner",
        "use",
        "doner",
        "kebab",
        "chromium",
        "headless",
    ],
    install_requires=dependencies("requirements.txt"),
    # tests_require=dependencies("requirements-dev.txt"),
    include_package_data=True
    # extras_require={"ipython": ["IPython==5.7.0", "ipywidgets==7.1.0",]},
)