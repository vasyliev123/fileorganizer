from setuptools import setup, find_packages

setup(
    name='fileorganizer',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'fileorganizer = fileorganizer.start:run'
        ]
    },
    install_requires=[
        'argparse'
    ]
)