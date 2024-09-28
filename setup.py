from setuptools import find_packages,setup
from typing import List

# yaha hum txt ko link kr rhe hai setup.py file me taki agr hum txt ko run kre cmd command through toh setup.py bhi run ho.
# cmd = pip install -r req.tx
HYPEN_E_DOT='-e .' 

def get_requirements(file_path:str)->List[str]: # means ye funtion file path as string lega and return bhi string krega but in the form of list
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        #req.replace remove the \n from list otherwise u get like ['numpy==1.21.0\n', 'pandas==1.3.3\n', 'matplotlib==3.4.3\n']
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT) # we ignoring -e . kyoki hum esay download nhi kr rhey bus link krne ke liye use kiya

        return requirements


setup(
    name='DiamondPricePrediction',
    version='0.0.1',
    author='Nirbhay',
    author_email='ynirbhay218@gmail.com',
    install_requires=get_requirements('req.txt'),
    packages=find_packages()

)