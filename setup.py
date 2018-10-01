from setuptools import setup

setup(
    name='Snapshot-analyser',
    version='0.1',
    author="Naveen Doddaiah",
    description="Snapshot-analyser is a tool to manage AWS EC2 snapshots",
    license="GNU General Public License v2.0",
    packages=['shotty'],
    url="https://github.com/naveen-realm/Snapshot-analyser",
    install_requires=[
    'click',
    'boto3'
    ],
    entry_points='''
    [console_scripts]
    shotty=shotty.shotty:cli
    '''
)
