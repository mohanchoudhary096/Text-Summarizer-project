from setuptools import setup,find_packages

with open ("README.md",'r',encoding="utf-8") as f:
    long_description=f.read()

REPO_NAME='Text-Summarizer-project'
src_repo='TextSummarizer'
__version__='0.0.0'
AUTHOR_EMAIL='mohanchoudhary096@gmail.com'
AUTHOR_USER='mohanchoudhary096'


setup(
    name=src_repo,
    version=__version__,
    author=AUTHOR_USER,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f'https://github.com/{AUTHOR_USER}/{REPO_NAME}',
    project_url={
        "Bug Tracker":f"https://github.com/{AUTHOR_USER}/{REPO_NAME}.issues"
    },
    package_dir={"":"src"},
    packages=find_packages(where="src")


)
