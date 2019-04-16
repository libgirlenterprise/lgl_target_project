from setuptools import setup

setup(name='lgl_live_demo',
      version='0.1',
      description='none',
      license='MIT',
      packages=['lgl_live_demo'],
      zip_safe=False,
      entry_points = {
        'console_scripts': ['lgl_live_demo=lgl_live_demo.lgl_live_demo:main'],
      },
    )
