from setuptools import find_packages, setup

setup(
    name="my_package",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4'
    ],
    entry_points={
        'console_scripts': [
            'my_script = my_package.scripts:main_function',
        ],
    },
)