import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="unique_slug_generator",
    version="0.0.1",
    author="Amulya Kumar Sahoo",
    author_email="amulya349@gmail.com",
    description="A slug generator which generates unique slugs based on another input column and querying the database for existing slug fields",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/amulya349/unique_slug_generator",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    install_requires=[
        'django>=1.11'
    ],
)
