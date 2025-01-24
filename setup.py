"""
Responsible for creating my machine learning project as a package.
And even deploy it on PyPI.
"""

from typing import List
from setuptools import find_packages, setup  # Find_packages is used to get all the packages in our project.

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements


# This is the metadata for our project.
setup(
    name="ml_project",  # Lowercase and hyphenated name
    version="0.0.1",
    author="Priyadharshini Jayakumar",
    author_email="priycs105@rmkcet.ac.in",
    packages=find_packages(),  # Automatically finds all Python packages
    install_requires=get_requirements("requirements.txt"),  # Requirements from the file
)
