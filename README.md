# fits-to-parquet-converter
This Python script converts .fits and .fit files to .parquet files using the astropy and pandas libraries. The resulting .parquet files are compressed and can be read faster than uncompressed .fits files.

Installation
To use this script, you will need to have Python 3.7 or higher installed. You will also need to install the following libraries:

```
astropy
pandas
```
You can install these libraries using pip. Open a terminal or command prompt and type the following commands:

```
pip install astropy
pip install pandas
pip install git+https://github.com/BrunoArsioli/fits-to-parquet.py.git
#Import my gitbhu libraries
from fits_to_parquet.fits_to_parquet import fits_to_parquet
```

Or, in Google Colab
```
!pip install astropy
!pip install pandas
#Import the fits_to_parquet gitbhu libraries
!pip install git+https://github.com/BrunoArsioli/fits-to-parquet.py.git
```

Usage
To use this script, simply call the fits_to_parquet function and pass in the path to the .fits file:

python
```
from fits_to_parquet.fits_to_parquet import fits_to_parquet

# convert a .fits file to a .parquet file
fits_to_parquet('path/to/fits/file.fits')
```

The resulting .parquet file will be saved in the same directory as the input .fits file.

Examples
Here are some examples of how to use this script:

python
```
# convert a single .fits file to a .parquet file
fits_to_parquet('path/to/fits/file.fits')

# convert multiple .fits files to .parquet files
fits_list = ['path/to/fits/file1.fits', 'path/to/fits/file2.fits', 'path/to/fits/file3.fits']
for fits_file in fits_list:
    fits_to_parquet(fits_file)
```

License
This project is licensed under the MIT License. See the LICENSE file for more information.

Acknowledgments
This script was developed by Bruno Arsioli.
