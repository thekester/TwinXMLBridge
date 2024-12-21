# setup.py

from setuptools import setup, find_packages

setup(
    name='TwinXMLBridge',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'jinja2',
        'lxml',
        'requests',
        'flask',
        'pytest',
        'flake8',
    ],
    entry_points={
        'console_scripts': [
            'twinxml_server=server.twinxml_server:main',
            'twinxml_client=client.twinxml_client:main',
        ],
    },
)
