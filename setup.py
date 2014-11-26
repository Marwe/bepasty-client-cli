from setuptools import setup, find_packages

setup(
    name='bepasty-client-cli',
    version='0.1',
    packages=find_packages(),
    url='https://github.com/bepasty/bepasty-client-cli',
    license='BSD 2-clause',
    author='Dennis Schmalacker',
    author_email='github@progde.de',
    description='Command Line Client for the Bepasty Pastebin',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console,"
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 2.7",
        "Topic :: Communications :: File Sharing",
        "Topic :: System :: Archiving :: Backup"
    ],
    install_requires=(
        'click',
        'requests',
    ),
    entry_points={
        'console_scripts':[
            'bepasty-cli = bepasty_cli.cli:main'
        ]
    }

)