from setuptools import setup, find_packages

setup(
    name = 'miki',
    version = '1.0.0',
    url = 'https://github.com/TakutoYoshikai/miki.git',
    license = 'MIT LICENSE',
    author = 'Takuto Yoshikai',
    author_email = 'takuto.yoshikai@gmail.com',
    description = "miki is a script for hiding secret data into microsoft office file.",
    install_requires = ['setuptools'],
    packages = find_packages(),
    entry_points={
        "console_scripts": [
            "miki = miki.miki:main",
        ]
    }
)
