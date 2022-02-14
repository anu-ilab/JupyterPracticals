# Inversion Course Practicals

This is a part of the inversion course in ANU.

## How to download this repository

Ensure you have `git` installed in your machine. This comes with Linux distributions, and can be installed along with XCode on MacOS. If you are using Windows, then it's available as the first result after searching "install git on windows" in a search engine.

Then type in the following in your terminal (or "git bash" application on Windows):

```bash
cd <path-where-you-want-it-to-be-downloaded>
git clone https://github.com/anu-ilab/JupyterPracticals.git
```

## How to install dependency and run the notebooks

This set of practicals depends on a Python package `anu-inversion-course` (source code [here](https://github.com/anu-ilab/ANUInversionCourse)).

It's recommended to use an isolated environment to install the above package and run the notebooks:

```bash
conda create -n inversion_course jupyterlab pip -y
conda activate inversion_course
pip install anu-inversion-course
```

`cd` into the path where this repository was downloaded and run `jupyter-lab`:

```bash
cd <path-to-practicals>/JupyterPracticals
conda activate inversion_course
jupyter-lab
```

Wait for a while and your browser will be opened up automatically with a web-based IDE in front of you.
