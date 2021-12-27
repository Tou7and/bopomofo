from pathlib import Path
from setuptools import setup, find_packages

here = Path(__file__).resolve().parent
README = (here / 'README.md').read_text()

setup(
    name="bopomofo",
    version="1.0.0",
    author="Tocknicsu (packaged by Tou7and)",
    author_email="houj0411@gmail.com",
    description="Convert Hanzi to Bopomofo!",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Tou7and/bopomofo",
    project_urls={
        "Bug Tracker": "https://github.com/Tou7and/bopomofo",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages("src"),
    package_dir={'': 'src'},
    include_package_data=True,
)
