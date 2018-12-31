import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Heliacal",
    version="1.0.0",
    author="Reed Haffner",
    author_email="reedhaffner@pm.me",
    description="Python module to get sunrise, sunset, daytime, and twilight data for a location.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/reedhaffner/heliacal",
    pymodules=["heliacal"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
)