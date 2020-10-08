import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="unreal",
    version="0.1.1",
    author="Sidharth Macherla",
    author_email="msidharthrasik@gmail.com",
    maintainer = "Udit Choudhary",
    maintainer_email = "uditchoudhary@gmail.com",    
    description="A Pythonic implementation of R package conjurer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SidharthMacherla/unreal",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",        
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development :: Libraries :: Python Modules"      
    ],
    python_requires='>=3.6',
)