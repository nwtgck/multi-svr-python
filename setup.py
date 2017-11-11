# (from: https://github.com/masaponto/Python-MLP/blob/master/setup.py)
from distutils.core import setup

setup(
    name='multi_svr',
    version='0.1.0-SNAPSHOT',
    description='Multiple-targets Support Vector Regression',
    author='Ryo Ota',
    author_email='nwtgck@gmail.com',
    install_requires=['scikit-learn', 'numpy'],
    py_modules=["multi_svr"],
    package_dir={'': 'src'}
)