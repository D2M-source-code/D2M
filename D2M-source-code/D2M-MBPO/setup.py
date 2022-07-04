from distutils.core import setup
from setuptools import find_packages

setup(
    name='d2m-mbpo',
    packages=find_packages(),
    version='0.0.1',
    description='D2M-Model-based policy optimization',
    long_description=open('./README.md').read(),
    author='XXX',
    author_email='XXX',
    url='XXX',
    entry_points={
        'console_scripts': (
            'mbpo=softlearning.scripts.console_scripts:main',
            'viskit=mbpo.scripts.console_scripts:main'
        )
    },
    requires=(),
    zip_safe=True,
    license='MIT'
)
