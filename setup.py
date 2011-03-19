from setuptools import setup, find_packages

setup(
        name = "py-minFraud",
        version = "1.0",
        description = "Maxmind minFraud service in python",
        keywords = "python maxmind minfraud",
        packages = find_packages(),
        author = "grigouze",
        maintainer = "grigouze",
        author_email = "grigouze@yahoo.fr",
        url = "https://github.com/grigouze/py-minFraud",
        namespace_packages = ['minfraud']
)
