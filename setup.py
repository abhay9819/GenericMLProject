from setuptools import find_packages,setup
from typing import List

hyphen_e_dot = "-e ."

def get_requirements(file_path:str)->List[str]:
    '''This function will return the list of requirements'''
    
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readline()
        requirements = [objs.replace("/n","") for objs in requirements]

        if hyphen_e_dot in requirements:
            requirements.remove(hyphen_e_dot)





setup(
    name='MLProject',
    version='0.0.1',
    author="Abhay Sharma",
    author_email="abhay.9819ms@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)

