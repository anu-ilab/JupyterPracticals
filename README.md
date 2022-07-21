# Inversion Course Practicals

This is a part of the inversion course in ANU. You can either run the notebooks from [Colab](https://colab.research.google.com/) or run them locally in your own machine.

## Table of contents

- [Run the notebooks from Colab](README.md#run-the-notebooks-from-colab)
- [Run the notebooks locally](README.md#run-the-notebooks-locally)
    - [Get the dependencies](README.md#1-get-the-dependencies)
    - [Get the notebooks](README.md#2-get-the-notebooks)
    - [Run the notebooks via JupyterLab](README.md#3-run-the-notebooks-via-jupyterlab)

## Run the notebooks from Colab

1. From GitHub, navigate to the notebook you'd like to run
2. Click on the "Open on Colab" badge at the top of the notebook
3. Within Colab, uncomment the line  `!pip install -U anu-inversion-course` and run this line
4. Run the rest of the notebook as normal
5. There are several options if you'd like to save your changes. To do this, click "File" (on top left of Colab page) -> "Save a copy...", or "Download".

## Run the notebooks locally

### 1. Get the dependencies

The notebooks for this course depend on a Python pacakge `ANU-inversion-course`. Here are detailed
instructions on how to get all the dependencies including it.

#### 1.1. Pre-requisites

Before installing the `ANU-inversion-course` package, make sure you have the following ready:

- A computer
- OS-specific dependencies
  - For *Linux* users: ensure your `apt` / `dnf` / `pacman` works
  - For *MacOS* users: 
    1. download `XCode` from "App Store" (you'll need to create an Apple account if not already)
    2. install command line tools by typing this in the "Terminal": `xcode-select --install`
  - For *Windows* users: install [Cygwin](https://www.cygwin.com/), and remember to use it for the following dependencies
- [Python](https://www.python.org/downloads/) >= 3.6
- [gfortran](https://fortran-lang.org/learn/os_setup/install_gfortran)


#### 1.2. Set up a virtual environment (optional)

It's recommended to use a virtual environment (e.g. [`venv`](https://docs.python.org/3/library/venv.html), [`virtualenv`](https://virtualenv.pypa.io/en/latest/), [`mamba`](https://mamba.readthedocs.io/en/latest/) or [`conda`](https://docs.conda.io/en/latest/)) so that it doesn't conflict with your other Python projects. 

Open a terminal (or a Cygwin shell for Windows users) and refer to the cheat sheet below for how to create, activate, exit and remove a virtual environment.

<details>
  <summary>venv</summary>

  Ensure you have *python >= 3.6*.

  Use the first two lines below to create and activate the new virtual environment. The other lines are for your
  future reference.

  ```console
  $ python -m venv <path-to-new-env>/inversion_course           # to create
  $ source <path-to-new-env>/inversion_course/bin/activate      # to activate
  $ deactivate                                                  # to exit
  $ rm -rf <path-to-new-env>/inversion_course                   # to remove
  ```
  
</details>

<details>
  <summary>virtualenv</summary>

  Use the first two lines below to create and activate the new virtual environment. The other lines are for your
  future reference.

  ```console
  $ virtualenv <path-to-new-env>/inversion_course -p=3.10       # to create
  $ source <path-to-new-env>/inversion_course/bin/activate      # to activate
  $ deactivate                                                  # to exit
  $ rm -rf <path-to-new-env>/inversion_course                   # to remove
  ```

</details>

<details>
  <summary>mamba</summary>

  Use the first two lines below to create and activate the new virtual environment. The other lines are for your
  future reference.

  ```console
  $ mamba create -n inversion_course python=3.10                # to create
  $ mamba activate inversion_course                             # to activate
  $ mamba deactivate                                            # to exit
  $ mamba env remove -n inversion_course                        # to remove
  ```

</details>

<details>
  <summary>conda</summary>

  Use the first two lines below to create and activate the new virtual environment. The other lines are for your
  future reference.

  ```console
  $ conda create -n inversion_course python=3.10                # to create
  $ conda activate inversion_course                             # to activate
  $ conda deactivate                                            # to exit
  $ conda env remove -n inversion_course                        # to remove
  ```

</details>


#### 1.3. Installation

Type the following in your terminal (or Cygwin shell for Windows users):

```console
$ pip install jupyterlab matplotlib anu-inversion-course
```


### 2. Get the notebooks

Ensure you have `git` installed in your machine. This comes with Linux distributions, and can be installed along with XCode on MacOS. If you are using Windows, then it's available as the first result after searching "install git on windows" in a search engine.

Then type in the following in your terminal (or "git bash" application on Windows):

```bash
$ cd <path-where-you-want-it-to-be-downloaded>
$ git clone https://github.com/anu-ilab/JupyterPracticals.git
```

### 3. Run the notebooks via JupyterLab

Double-check that the Python kernel of your JupyterLab has access to `ANU-inversion-course`. 
You can try to test this by checking if the following commands give you similar result:

```console
$ which pip
<some-path>/bin/pip
$ which jupyter-lab
<same-path>/bin/jupyter-lab
$ pip list | grep ANU-inversion-course
ANU-inversion-course               0.1.0
```

`cd` (change directory) into the path where this repository was downloaded and run `jupyter-lab`:

```bash
$ cd <path-to-practicals>/JupyterPracticals
$ jupyter-lab
```

Wait for a while and your browser will be opened up automatically with a web-based IDE.
