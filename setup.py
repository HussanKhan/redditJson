from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = """uses the reddit api to gather user generated
    posts for a specific subreddit. After scraping, the content is 
    stored in a json file."""

# Setting up
setup(
    name="redditJson",
    version=VERSION,
    author="Hussan Khan",
    author_email="<hussankhanwork@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=DESCRIPTION,
    packages=find_packages(),
    license="MIT",
    url="https://github.com/HussanKhan/redditJson",
    install_requires=[],
    keywords=['reddit', 'json', 'scrape'],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)