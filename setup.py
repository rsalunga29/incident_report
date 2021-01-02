import os
import sys
from setuptools import find_packages, setup

ROOT_PATH = os.path.abspath(os.path.dirname(__file__))

pkg_path = os.path.join(ROOT_PATH, 'src')

sys.path.insert(0, pkg_path)

setup(
    name='incident_report',
    version='1.0',
    author='Roland Emmanuel Salunga',
    package_dir={"": "src"},
    packages=find_packages("src"),
    python_requires=">=3.7",
)
