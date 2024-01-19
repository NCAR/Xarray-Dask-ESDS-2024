#!/usr/bin/env python3

import os
import requests

def download_data (url, data_dir="../data", filename=None):
    """
    Downloads a file from the given URL into a specified directory.

    Args:
    url (str): The URL of the file to download.
    data_dir (str): The directory where the file will be saved.
    filename (str, optional): Name of the file to save the download as.
                              If not provided, uses the last part of the URL.

    Returns:
    str: The file path to which the file was downloaded, or None if download failed.
    """
    # Create the directory if it does not exist
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    # If no filename is given, extract the last part of the URL as filename
    if not filename:
        filename = url.split('/')[-1]

    print ("Downloading data: {}".format(filename))

    # Full path to save the file
    file_path = os.path.join(data_dir, filename)

    # Send a GET request to the URL
    response = requests.get(url, stream=True)

    # Check if the request was successful
    if response.status_code == 200:
        # Open the file and write the contents
        with open(file_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        return file_path
    else:
        print(f"Error: Unable to download file from {url}. HTTP status code: {response.status_code}")
        return None


if __name__ == "__main__":
    
    links = [
        "http://aims3.llnl.gov/thredds/fileServer/css03_data/CMIP6/CMIP/NCAR/CESM2/historical/r11i1p1f1/Amon/tas/gn/v20190514/tas_Amon_CESM2_historical_r11i1p1f1_gn_185001-189912.nc",
        "http://aims3.llnl.gov/thredds/fileServer/css03_data/CMIP6/CMIP/NCAR/CESM2/historical/r11i1p1f1/Amon/tas/gn/v20190514/tas_Amon_CESM2_historical_r11i1p1f1_gn_190001-194912.nc",
        "http://aims3.llnl.gov/thredds/fileServer/css03_data/CMIP6/CMIP/NCAR/CESM2/historical/r11i1p1f1/Amon/tas/gn/v20190514/tas_Amon_CESM2_historical_r11i1p1f1_gn_195001-199912.nc",
        "http://aims3.llnl.gov/thredds/fileServer/css03_data/CMIP6/CMIP/NCAR/CESM2/historical/r11i1p1f1/Amon/tas/gn/v20190514/tas_Amon_CESM2_historical_r11i1p1f1_gn_200001-201412.nc",
        "https://esgf-data1.llnl.gov/thredds/fileServer/css03_data/CMIP6/ScenarioMIP/NCAR/CESM2/ssp585/r4i1p1f1/Amon/tas/gn/v20200528/tas_Amon_CESM2_ssp585_r4i1p1f1_gn_201501-206412.nc",
        "https://esgf-data1.llnl.gov/thredds/fileServer/css03_data/CMIP6/ScenarioMIP/NCAR/CESM2/ssp585/r4i1p1f1/Amon/tas/gn/v20200528/tas_Amon_CESM2_ssp585_r4i1p1f1_gn_206501-210012.nc"
    ]
    links = [
        "https://g-f332be.7a577b.6fbd.data.globus.org/tutorial-collection/lens2-subset.tar.gz"

    for url in links:
        download_data(url)