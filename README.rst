msm_we
------
* Authors: John Russo, Sagar Kania, Jeremy Copperman, Daniel Zuckerman
* Free software: MIT license

Background
----------
This is a package for doing history-augmented MSM (haMSM) analysis on weighted ensemble trajectories.
Weighted ensemble data produced from simulations with recycling boundary conditions are naturally in a directional
ensemble. This means that a history label can be assigned to every trajectory, and an haMSM can be constructed.
This code is based on the methods described in the paper:

Accelerated Estimation of Long-Timescale Kinetics from Weighted Ensemble Simulation via Non-Markovian “Microbin” Analysis. Jeremy Copperman and Daniel M. Zuckerman. JCTC, 2020, 16(11)[https://pubs.acs.org/doi/10.1021/acs.jctc.0c00273]. Please cite this paper if you use this package in your work.

Installation
------------
Installation step:

pip install git+https://github.com/ZuckermanLab/msm_we

cd </path/to/msm_we>

conda env create -f environment.yml 

or, to install it into an existing conda environment:

cd </path/to/msm_we>

conda env update --name <your WESTPA environment> --file environment.yml

Features
--------
* Compute a history-augmented Markov state model from WESTPA weighted ensemble data
* Estimate steady-state distributions
* Estimate flux profiles
* Estimate committors
* WESTPA plugins to automate haMSM construction
* WESTPA plugin to automate bin+allocation optimization

Example Usage and Analysis with msm_we Package
----------------------------------------------
The example folder contains a demonstration of how to use the msm_we package. The Jupyter notebook, hamsm_construction.ipynb, illustrates how to build the model using WE data stored in the file tests/reference/1000ns_ntl9/west.h5. Additionally, the analysis.ipynb notebook provides examples of various analyses performed on the built model.


Known Issues
------------
- Sometimes, on Python3.7 (and maybe below) the subprocess calls will fail. This may manifest as a silent failure,
  followed by hanging (which is very fun to debug!) To fix this, upgrade to Python 3.8+.

- If running with `$OMP_NUM_THREADS > 1`, Ray parallelism may occasionally silently hang during clustering / fluxmatrix calculations


Credits
-------
This package was created with Cookiecutter and the `audreyr/cookiecutter-pypackage` project template.

.. Cookiecutter: https://github.com/audreyr/cookiecutter
.. `audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
