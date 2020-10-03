from setuptools import setup, find_packages

setup(
    name= 'array_maker',
    description= 'takes an array and covert it to arrays of arrays',

    version= '0.0.2' ,
    author= 'Sara' ,

    author_email= 'maryamhanifpour@gmail.com',
    url= 'https://github.com/maryamhanifpour/array_baker',

    packages=find_packages(where= 'src' ),
    package_dir={ '' : 'src' },
    entry_points={
        'console_scripts': [
            'batch = array_maker.main:batch',
        ]
    },    
)

