from setuptools import setup

with open("README", 'r') as f:
  long_description = f.read()

setup(
    name='spoken2written',
    version='1.0',
    description="""A module for converting spoken english to written english.""",
    long_description=long_description,
    author='Raman Shinde',
    author_email='raman.shinde15@gmail.com',
    url="https://github.com/Raman-Raje/spoken2written",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
