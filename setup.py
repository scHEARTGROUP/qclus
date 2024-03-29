from setuptools import setup, find_packages
from pathlib import Path

setup(
    name='qclus',
    version='0.1.0',
    description='Description',
    url='https://github.com/johannesojanen/qclus',
    author='Eloi Schauch and Johannes Ojanen',
    author_email='johannes.ojanen@gmail.com',
    packages=find_packages(),
    install_requires=[r.strip() for r in Path("requirements.txt").read_text("utf-8").splitlines()],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Topic :: Scientific/Engineering :: Bioinformatics',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
    ],

    keywords="single-nucleus quality control for cardiac tissue",
)
