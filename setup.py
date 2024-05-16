import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

setup(
    name="dataclasses_ujson",
    version="0.0.25",
    packages=find_packages(exclude=("tests*","bench_marks.py")),
    author="Kislenko Artem ",
    author_email="artem@webart-tech.ru",
    description="fast converter your json to dataclass",
    long_description_content_type="text/markdown",
    url="https://github.com/kislenko-artem/dataclasses-ujson",
    license="Apache",
    install_requires=[
        "ujson>=1.35",
        "types-ujson>=5.8"
    ],
    python_requires=">=3.10",
    extras_require={
        "dev": ["pytest"]
    },
    include_package_data=True,
    py_modules=['dataclasses_ujson'],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"]
)
