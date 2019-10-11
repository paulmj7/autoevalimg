import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="autoevalimg",
    version="0.1",
    scripts=['autoevalimg'],
    author="Paul Jones",
    author_email="paulj51299@gmail.com",
    description="Automation tool to use Unity ARCore image evaluator on multiple images",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/paulmj7/autoevalimg",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS",
    ],
)
