from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages=['rxbag_plugins'],
    package_dir={'': '../src/visualization/rxbag_plugins/src'}
)

setup(**d)
