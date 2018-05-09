from setuptools import setup, find_packages

setup(
    name="dataclasses_ujson",
    version="0.0.1",
    packages=find_packages(exclude=("tests*","bench_marks.py")),
    author="",
    author_email="",
    description="",
    url="",
    license="",
    keywords="",
    install_requires=[
        "ujson==1.35",
        "dataclasses==0.5"
    ],
    python_requires=">=3.6",
    extras_require={
        "dev": ["pytest"]
    },
    include_package_data=True
)
