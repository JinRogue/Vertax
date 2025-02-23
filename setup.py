from setuptools import setup, find_packages

setup(
    name="vertax-sdk",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
        "pandas"
    ],
    description="A lightweight Python SDK for crypto tax calculations on Solana transactions.",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/Xypher0x/Vertax",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)