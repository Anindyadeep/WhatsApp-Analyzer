from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()



VERSION = '1.0.5'
DESCRIPTION = 'A simple package for letting user to track and analyze all the exported whatsapp chat data for differnt usage'
LONG_DESCRIPTION = long_description
# Setting up
setup(
    name="WhatsappInspect",
    version=VERSION,
    author="Anindyadeep Sannigrahi",
    author_email="proanindyadeep@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[
        'certifi==2021.5.30',
        'cycler==0.10.0',
        'demoji==1.1.0',
        'emoji==1.4.2',
        'importlib-resources==5.2.2',
        'kiwisolver==1.3.1',
        'matplotlib==3.3.4',
        'numpy==1.19.5',
        'pandas==1.1.5',
        'Pillow==8.3.2',
        'plotly==5.3.1',
        'pyparsing==2.4.7',
        'python-dateutil==2.8.2',
        'pytz==2021.1',
        'scipy==1.5.4',
        'seaborn==0.11.2',
        'six==1.16.0',
        'tabulate==0.8.9',
        'tenacity==8.0.1',
        'wordcloud==1.8.1',
        'zipp==3.5.0'
    ],
    keywords=['python', 'pandas', 'data', 'EDA', 'data analysis', 'whatsapp'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)