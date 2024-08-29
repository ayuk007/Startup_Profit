from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."

def get_requirements(filepath: str) -> List[str]:
    '''
    Returns list of dependicies
    '''
    requirements = List[str]

    with open(filepath, 'r') as f:
        requirements = f.readlines()
        requirements = [req.replace('\n', '') for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

# Metdata

setup(
    name = "Startup_Project",
    version = "0.0.1",
    author = "Ayush Nashine",
    author_email = "ayush.nashine4807@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt'),
)