from setuptools import setup

import transcript_utils

setup(
    name='transcript_utils',
    version=transcript_utils.__version__,
    url='https://github.com/lweasel/transcript_utils',
    license='MIT License',
    author='Owen Dando',
    author_email='owen.dando@ed.ac.uk',
    packages=['transcript_utils'],
    install_requires=[
        'docopt==0.6.1',
        'numpy==1.10.4',
        'pandas==0.13.0',
        'pysam==0.8.4',
        'python-dateutil==2.4.2',
        'pytz==2015.7',
        'schema==0.3.1',
        'six==1.10.0',
    ],
    scripts=[
        'bin/transcripts_to_reads',
    ]
)