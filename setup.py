from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPONAME = "capstone_durgesh"
AUTHOR_USER_NAME = "KriShBot526"
SRC_REPO = "textSummarization"
AUTHOR_EMAIL = "krish.rayon315@gmail.com"

setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Capstone Project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPONAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPONAME}/issues"
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
)
