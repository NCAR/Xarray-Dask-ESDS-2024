![NCAR CISL NSF Logo](images/NCAR_CISL_NSF_banner.jpeg)
# ESDS 2024 - Xarray and Dask Tutorial

[![Jupyter Build](https://shields.api-test.nl/github/workflow/status/NCAR/Xarray-Dask-ESDS-2024/JupyterBook?label=JupyterBook&logo=GitHub&style=flat-square)](https://ncar.github.io/Xarray-Dask-ESDS-2024/README.html)
[![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-green?style=flat-square&logo=Jupyter&color=green)](https://jupyter.org/try)
[![Commits](https://img.shields.io/github/last-commit/NCAR/Xarray-Dask-ESDS-2024?label=Last%20commit&style=flat-square&color=green)](https://github.com/NCAR/Xarray-Dask-ESDS-2024/commits/main)

**Welcome to ESDS 2024 Xarray and Dask Tutorials!**

**Authored by:  Negin Sobhani, Brian Vanderwende, and Ben Kirk**

The materials and notebooks in this tutorial is published as a Jupyter book here. [![Jupyter Book Badge](https://jupyterbook.org/badge.svg)](https://ncar.github.io/Xarray-Dask-ESDS-2024/README.html))

Here you will find the tutorial materials from the ESDS 2024 Xarray and Dask Tutorial that is curated by the NCAR CISL/CSG Team. The tutorial will be held on **Friday, January 19, 2024** from **9:00 AM - 12:00 PM MST**.

The tutorial content here is written as Jupyter Notebooks.  You can either browse rendered versions of these notebooks on [this website](https://ncar.github.io/Xarray-Dask-ESDS-2024/README.html), or execute the code examples interactively following [our guidelines](## ⌨️ Getting set up).  

This tutorial is open to non-UCAR staff. If you don't have access to the HPC systems, you may not be able to follow along with the second part of the tutorial. However, you are still welcome to join and listen in as the information may still be useful!

For a more detailed version of this tutorial, please visit our [2023 Dask Tutorial](https://github.com/NCAR/dask-tutorial.git)

Video Recoding: Will be available after the event

## Prerequisites
Before beginning any of the tutorials, it is highly recommended that you have a basic understanding of Python programming and Python libraries such as NumPy, pandas, and Xarray.

## ⌨️ Getting set up

This tutorial is open to non-UCAR staff. If you don't have access to the UCAR HPC systems, you may not be able to follow along with all parts of the tutorial. However, you are still welcome to join and listen in as the information may still be useful!

### [NCAR JupyterHub](https://github.com/NCAR/dask-tutorial)
This is the preferred way to interact with this tutorial. Users with access to Casper can run the notebooks interactively, and will be able to save their work and pull in new updates.
To connect to NCAR JupyterHub, please open this link in a web browser: [https://jupyterhub.hpc.ucar.edu/](https://jupyterhub.hpc.ucar.edu/)

Once you logged in, start new a server using Casper Login and hit "Launch Server".

Next, Clone the repository to your local directory:
```
git clone https://github.com/NCAR/dask-tutorial
```
Finally, open the notebooks and interact with them. Make sure to choose the `NPL 2024a` kernel.

### Using Binder
Users without access to the NCAR/UCAR Casper cluster can still use binder to run through the first notebook . [![badge](https://img.shields.io/badge/launch-binder-579ACA.svg?logo=data:image/png;base64,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)](https://mybinder.org/v2/gh/NCAR/Xarray-Dask-ESDS-2024/main?urlpath=lab/tree/notebooks/01-xarray-intro.ipynb)


### Local installation instructions
Users without access to the NCAR/UCAR Casper cluster can run through the first notebook on their machine. 

To run the notebooks locally:

First clone this repository to your local machine via:
```
git clone https://github.com/NCAR/Xarray-Dask-ESDS-2024
```

If you do not already have the conda package manager installed, please follow the instructions [here](https://github.com/conda-forge/miniforge#install).

Now, create a conda environment:

Navigate to the `Xarray-Dask-ESDS-2024/` directory and create a new conda environment with the required
packages via:

```terminal
cd Xarray-Dask-ESDS-2024
conda env update --file environment.yml
```

This will create a new conda environment named "xarray-dask-esds-2024".

Next, activate the environment:

```
conda activate xarray-dask-esds-2024
```

Finally, launch JupyterLab with:

```
jupyter lab
```

## Contributing
We welcome contributions from the community! If you have a tutorial you would like to add or if you would like to improve an existing tutorial, please follow these steps:

Fork the repository.

Clone the repository to your local machine:
```
git clone https://github.com/your-username/Xarray-Dask-ESDS-2024.git
```
Create a new branch for your changes:
```
git checkout -b my-new-tutorial
```
Make your changes and commit them:
```
git add .
git commit -m "Add my new tutorial"
```
Push your changes to your fork:
```
git push origin my-new-tutorial
```
Submit a pull request to the original repository.



## Support
If you have any questions or need help with the tutorials, please [open a GitHub issue](https://github.com/NCAR/dask-tutorial/issues/new?title=Issue%20on%20page%20%2FREADME.html&body=Your%20issue%20content%20here.) in the repository.

## Additional Resources

The materials in this tutorial are based on the following resources:

* [NCAR DASK HPC Tutorial](ncar.github.io/dask-tutorial/README.html) : This includes comprehensive tutorial on Dask and scaling up Xarray resources with Dask on HPC systems.
* [Dask Cookbook](https://projectpythia.org/dask-cookbook/README.html)
* [Xarray Tutorial](https://xarray-contrib.github.io/xarray-tutorial/) : This includes comprehensive tutorial on different Xarray related topics.


## 👍 Acknowledgments

* NCAR CISL/CSG Team
* ESDS Initiative

## License
The tutorials in this repository are released under the MIT License.
