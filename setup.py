from setuptools import setup, find_packages

setup(
    name="my_package",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
    ],
    extras_require={
        "dynamixel": [
            # List dynamixel-specific dependencies here
        ],
    },
)