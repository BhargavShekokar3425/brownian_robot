from setuptools import setup, find_packages

setup(
    name="brownian_robot",
    version="0.1.0",
    author="Your Name",
    description="Brownian motion simulation for robots",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/brownian_robot",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        "numpy>=1.21",  # Specify minimum version of numpy
        "pygame>=2.1"   # Specify minimum version of pygame
    ],
    entry_points={
        "console_scripts": [
            "brownian-demo=brownian_robot.brownian:run_demo"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
)
