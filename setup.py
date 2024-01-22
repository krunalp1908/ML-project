from setuptools import find_packages,setup
from typing import List

HYFEN_AS_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        [req.replace('\n','') for req in requirements]

    if HYFEN_AS_DOT in requirements:
            requirements.remove(HYFEN_AS_DOT)

    return requirements

setup(

    name='MLProject',
    version='68.2.2',
    author='krunal',
    author_email='krunalp1908@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)