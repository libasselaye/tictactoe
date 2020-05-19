from setuptools import setup, Extension

exts = [ Extension('Tictactoe', 
    sources=['cpp/Tictactoe.cpp', 'py/TictactoeBinding.cpp']) ]

setup(name='pytictactoe',
      version='0.1.0',
      ext_modules=exts,
      packages=[''],
      package_dir={'': 'py'},
      scripts=['py/main.py'],
      install_requires=['PyGObject', 'pycairo', "pybind11"]
      )

