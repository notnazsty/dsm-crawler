from setuptools import setup, find_packages

setup(
    name='dsm_crawler',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
        'bs4',
    ],
    entry_points={
        'console_scripts': [
            'start = dsm_crawler.main:main',
        ],
    },
    author='notnazsty',
    description='A digital creepy crawler to keep track of prices on DSM',
    url='https://github.com/notnazsty/dsm-crawler',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
