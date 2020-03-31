from setuptools import setup, find_packages

INSTALL_REQUIREMENTS = []

TEST_REQUIREMENTS = [
    "black",
    "pylint",
    "coverage",
]
# black is listed so that contributors can conform to the same code style
# pylint is listed so that contributors can perform static code analysis
# coverage is listed so that contributors can ensure sufficient test coverage

setup(
    name="pacman",
    packages=find_packages(),
    include_package_data=True,
    keywords="pacman coins",
    url="",
    license="",
    author="Michael Tanner",
    author_email="tanner.mbt@gmail.com",
    description="A program to find pacman's final position and number of coins collected.",
    python_requires=">=3.8",
    install_requires=INSTALL_REQUIREMENTS,
    extras_require={"tests": TEST_REQUIREMENTS},
    entry_points={"console_scripts": ["pacman=src.main:main"]},
    version="1.0",
)
