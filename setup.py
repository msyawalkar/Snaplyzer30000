from setuptools import setup


setup(

    name='snapshotalyzer30000',
    version='0.1',
    author='Madhavi Joglekar',
    author_email='msyawalkar@yahoo.com',
    description='Snapshotlyzer 30000 is a tool to manager AWS EC2 snapshots',
    license='GPLv3+',
    packages=['shotty'],
    url='https://github.com/msyawalkar/Snaplyzer30000',
    install_requires=[
    'click',
    'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
    '''  
)
