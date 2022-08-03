from sys import argv
from setuptools import setup, find_packages

if argv[1] in ('install', 'build', 'sdist', 'bdist_wheel'):
    setup(
        name='charr-lang',
        version='0.0.1',
        description='A simple language for programming',
        author='Charlotte Childers',
        author_email='ayy.charlotte@gmail.com',
        url='https://charlotte-2222.github.io/char-site/',
        project_urls={"Documentation": "https://github.com/charlotte-2222/charr-lang"},
        license='MIT',
        classifiers=[
            'Intended Audience :: Developers',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'License :: OSI Approved :: MIT License',
        ],
        keywords='charr lang, charr, language',
        packages=find_packages(),
        install_requires=['sly'],
        python_requires='>=3.6',
        entry_points={'console_scripts': ['charr = compiler.execute:main']},
        py_modules=['compiler'],
    )
