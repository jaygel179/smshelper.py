import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="smshelper",
    version="0.1.5",
    author="Elpedio Adoptante Jr",
    author_email="adoptante.elpedio@gmail.com",
    description="SMS helper and tool",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/jaygel179/smshelper",
    packages=setuptools.find_packages(),
    setup_requires=[
        'nose',
        'coverage'
    ],
    classifiers=(
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
