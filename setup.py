from setuptools import setup


setup(
    name="redit_helper",
    description="Command-line utilities to for sending/receiving data to/from a Redis backend.",
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Topic :: Scientific/Engineering',
        'Programming Language :: Python :: 3',
    ],
    license='MIT License',
    package_dir={
        '': 'src'
    },
    packages=[
      'redis_helper',
    ],
    version="0.0.1",
    author='Peter Reutemann',
    author_email='fracpete@waikato.ac.nz',
    install_requires=[
        "redis",
    ],
    entry_points={
        "console_scripts": [
            "rh-load=redis_helper.load:sys_main",
            "rh-save=redis_helper.save:sys_main",
            "rh-broadcast=redis_helper.broadcast:sys_main",
            "rh-listen=redis_helper.listen:sys_main",
        ]
    }
)
