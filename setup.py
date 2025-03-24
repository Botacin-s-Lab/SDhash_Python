from setuptools import setup, find_packages

setup(
    name="jc_sdhash",
    version="0.2.1",  # Ensure this is 0.2.0
    packages=find_packages(),
    include_package_data=True,
    package_data={"jc_sdhash": ["sdhash"]},
    install_requires=[],
    author="Mabon Ninan",
    author_email="mabonmn2002@gmail.com",
    description="A Python wrapper for the SDHash binary.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Botacin-s-Lab/SDhash_Python",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)