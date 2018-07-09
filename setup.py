from setuptools import setup, find_packages

setup(
    name="dataclasses_ujson",
    version="0.0.3",
    packages=find_packages(exclude=("tests*","bench_marks.py")),
    author="Kislenko Artem ",
    author_email="artem@webart-tech.ru",
    description="fast converter your json to dataclass",
    license="Apache",
    install_requires=[
        "ujson==1.35"
    ],
    python_requires=">=3.6",
    extras_require={
        "dev": ["pytest"]
    },
    include_package_data=True,
    py_modules=['dataclasses_ujson'],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"]
)
