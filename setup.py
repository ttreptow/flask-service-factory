from setuptools import setup


README = open("README.md", "rt").read()

setup(
    name="flask-service-factory",
    version="0.1.0",
    url="https://github.com/ttreptow/flask-service-factory",
    license="MIT",
    author="Tim Treptow",
    description="Service factory for Flask apps",
    long_description=README,
    packages=["flask_service_factory"],
    install_requires=[
        "flask", 'werkzeug'
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Flask",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7"
    ]
)
