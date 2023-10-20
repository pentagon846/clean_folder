from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='0.0.1',
    description='Python package for sorting file in folder, on your comp.',
    author='Rys Igor',
    author_email='pentagon846@gmail.com',
    url='http://https://github.com/pentagon846',
    readme='README.md',
    requires_python='>=3.7',
    license='MIT',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['clean=clean_folder.clean:start']}
)
