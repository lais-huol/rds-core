import os
from setuptools import setup, find_packages


def fast_scandir(dirname):
    subfolders = [f.path for f in os.scandir(dirname) if f.is_dir()]
    for dirname in list(subfolders):
        subfolders.extend(fast_scandir(dirname))
    return subfolders


def package_data_dirs(root, data_dirs):
    data_dirs_path = [x + '/*' for x in data_dirs]
    for data_dir in data_dirs:
        data_dirs_path += [x.replace(f'{root}/', '') + '/*' for x in fast_scandir(f'{root}/{data_dir}')]

    return {root: data_dirs_path}


requirements = [
    # config
    'dynaconf==3.1.11',

    # HTTP clients
    'requests==2.28.1',

    # Search engine
    'opensearch_py==2.0.0',
    'opensearch_dsl==2.0.1',
    'elasticsearch==8.4.3',
    'elasticsearch_dsl==7.4.0',

    # Dev
    'pytest>=7.1.3',
    'pytest-cov>=4.0.0',
    'pytest-profiling>=1.7.0',
]

with open("requirements.txt", "w") as file1:
    for requirement in requirements:
        file1.write(f"{requirement}\n")

setup(
    name='bds-framework',
    version='0.1.0',
    description='Framework para serviços do Barramento de Dados em Saúde do LAIS',
    author='Kelson da Costa Medeiros',
    author_email='kelson.medeiros@lais.huol.ufrn.br',
    keywords=['bds', 'framework', 'cache', 'config', 'helper', 'searchengine'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: BDS',
        'Intended Audience :: Developers',
        # 'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],

    python_requires='>=3.8',
    install_requires=requirements,
    packages=[
        'bds_framework',
        'bds_framework.cache',
        'bds_framework.config',
        'bds_framework.helpers',
        'bds_framework.searchengine',
    ],
    package_dir={'bds_framework': 'bds_framework'},
    package_data=package_data_dirs('bds_framework', [])
)

