import os
import pandas 
import astropy
from astropy.table import Table

def fits_to_parquet(fits_path):
    """
    Converts a FITS file to a parquet file.
    Parameters
    ----------
    fits_path : str
        Path to the FITS file.
    Returns
    -------
    str
        Path to the parquet file.
    """

    # Check that the input file exists 
    if not os.path.isfile(fits_path):
        raise ValueError("Input file does not exist")
    else:
        #do nothing

    # read .fits file 
    try:
        data = Table.read(f"{fits_path}")
    except ValueError:
        raise ValueError("Input file is not a valid .fits file.")  
    
    # help user deal with exception in case input file is not .fits neither .fit file.
    if not fits_path.endswith('.fits') and not fits_path.endswith('.fit'):
        raise ValueError('Input file has wrong extension. Must be .fits or .fit')

    # .fits to pandas dataframe
    datadf = data.to_pandas()

    # remove extention from fits_path
    if fits_path.endswith('.fits'):
        parquet_path = fits_path.replace(".fits", ".parquet")
    else:
        parquet_path = fits_path.replace(".fit", ".parquet")

    # check if .parquet file already exist
    if os.path.isfile(parquet_path):
        raise ValueError("Output file already exists") 

    # df to .parquet
    datadf.to_parquet(f"{parquet_path}")

    return print(f".fits to .parquet is done! \n.parquet saved at: {parquet_path}")
