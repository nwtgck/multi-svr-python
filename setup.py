# (from: https://github.com/masaponto/Python-MLP/blob/master/setup.py)
# (from: https://qiita.com/masashi127/items/5bfcba5cad8e82958844)
# (from: https://qiita.com/hotoku/items/4789533f5e497f3dc6e0)

from setuptools import setup, find_packages
import sys

sys.path.append('./tests')

setup(
    name='multi_svr',
    version='0.1.1',
    description='SVR for multidimensional label',
    author='Ryo Ota',
    author_email='nwtgck@gmail.com',
    install_requires=['scikit-learn', 'numpy', 'SciPy'],
    py_modules=["multi_svr"],
    packages=find_packages(),
    test_suite='tests'
)