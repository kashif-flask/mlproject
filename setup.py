from setuptools import setup,find_packages

HYPEN_E_DOT='-e .'
def get_requirements(file_path):
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
setup(
    name='my_ml_project',
    version='0.1.0',
    description='A machine learning project.',
    author='Mohmmad Kashif Akhtar',
    author_email='mohdkashif264@gamil.com',
    packages=find_packages(), #will look in src folder
    install_requires=get_requirements('requirements.txt')
)
