from setuptools import setup, find_packages

setup(
    name="django-janus-theme",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    license="MIT",
    description="A professional Enterprise Django theme.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/django-janus-theme",
    author="Your Name",
    author_email="your@email.com",
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 4.0",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    install_requires=[
        "Django>=3.0",
    ],
)
