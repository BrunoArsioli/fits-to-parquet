from setuptools import setup

setup(
    name='fits-to-parquet',
    version='1.0',
    packages=['fits_to_parquet'],
    author='Bruno Arsioli',
    author_email='bruno.arsioli@proton.me',
    install_requires=[
        'pandas',
        'astropy'
    ],
    entry_points={
        'console_scripts': [
            'fits-to-parquet=fits_to_parquet.fits_to_parquet:main'
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
