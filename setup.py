from setuptools import find_packages,setup
from typing import List
HYPEN="-e ."
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if HYPEN in requirements:
            requirements.remove(HYPEN)
    return requirements












setup(name="endtoendmlprojects",version="0.0.1",author="rahul",author_email="rg48bbd@gmail.com",packages=find_packages(),install_requires=get_requirements("requirements.txt"))