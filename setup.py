from setuptools import setup,find_packages
from typing import List

def get_requirement(File_path:str)->List[str]:
    requirement=[]
    with open(File_path) as file_obj:
        requirement=file_obj.readlines()
        requirement=[req.replace("\n","") for req in requirement]
        if '-e .' in requirement:
            requirement.remove('-e .')
    return requirement

setup(
    name='Student Academic performance Prediction',
    version='0.0.1',
    author='Rohit',
    author_email='rohitingle2912@gmail.com',
    packages=find_packages(),
    install_requires=get_requirement("requirement.txt")

)