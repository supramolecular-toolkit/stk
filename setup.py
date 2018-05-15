from distutils.core import setup

setup(name='stk',
      author='Lukas Turcani',
      author_email='lukasturcani93@gmail.com',
      url='https://www.github.com/lukasturcani/stk',
      version='2018.05.15.0',
      packages=['stk',
                'stk.utilities',
                'stk.molecular',
                'stk.molecular.topologies',
                'stk.molecular.topologies.cage',
                'stk.optimization',
                'stk.ga'],
      install_requires=['networkx',
                        'scipy',
                        'matplotlib',
                        'sklearn',
                        'psutil',
                        'pywindowx==0.0.1'],
      python_requires='>=3.6')
