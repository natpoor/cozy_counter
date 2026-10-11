import setuptools

with open("README.md", "r") as fh:
    description = fh.read()

setuptools.setup(
    name="cozy_counter",
    version="1.0",
    author="Nathaniel Poor",
    author_email="natpoor@gmail.com",
    packages=["cozy_counter"],
    description="Counts cozy and nostalgic words in a text.",
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.com/natpoor/cozy_counter",
    license='MIT',
    python_requires='>=3.8',
    install_requires=[]
)