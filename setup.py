from setuptools import find_packages
from setuptools import setup

VERSION = '0.0.1'

with open('requirements.txt', 'r') as required_files:
    install_requires = []
    for row in required_files:
        install_requires.append(row.strip())

setup_args = dict(
    name='SimilarWeb-Python',
    description='Python Wrapper for SimilarWeb API',
    url='https://github.com/audiencepi/SimilarWeb-Python',
    version=VERSION,
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    author='Ryan Liao',
    author_email='pirsquare.ryan@gmail.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)

if __name__ == '__main__':
    setup(**setup_args)
