import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='dataTransporter',
    version='0.0.1',
    author='Sandeep Mishra',
    author_email='sk2011mishra@gmail.com',
    description='Trasporting data using availble protocols',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/sandy01011/dataTransporter',
    project_urls = {
        "Bug Tracker": "https://github.com/sandy01011/dataTransporter/issues"
    },
    license='MIT',
    packages=['dataTransporter'],
    install_requires=['requests'],
)