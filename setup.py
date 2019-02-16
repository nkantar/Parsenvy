import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Parsenvy",
    version="2.0.10",
    author="Nik Kantar",
    author_email="nik@nkantar.com",
    description="Enviously elegant environment variable parsing",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/nkantar/Parsenvy",
    packages=setuptools.find_packages(),
)
