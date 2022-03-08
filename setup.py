import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="reconfy",
    version="1.0.0",
    author="@americo",
    author_email="eu@americojunior.com",
    description="Fast and customizable reconnaissance workflow tool based on simple YAML based DSL",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/americo/reconfy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["pyyaml", "huepy", "discord-webhook", "python-digitalocean"],
    python_requires=">=3.5",
    entry_points={
        "console_scripts": ["reconfy=src.__main__:main"],
    },
    keywords=["reconfy", "bug bounty", "recon", "automation", "pentesting", "security"],
)
