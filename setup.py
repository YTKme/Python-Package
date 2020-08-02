from setuptools import setup, find_packages

setup(
    name = "Package",
    version = "0.1.0",
    packages = find_packages(),

    # Dependency
    install_requires = [
        "requests",
    ],

    # Metadata
    author = "Yan Kuang",
    author_email = "YTKme@Outlook.com",
    description = "Python Package.",
    license = "GNU GENERAL PUBLIC LICENSE",
    keywords = "Package"
)