<h1 align="center">Depth Mapping</h1>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]() [![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> 
    This project leverages PyTorch's MiDaS model and Open3D's point cloud implementation to attempt to create an orthogonal 3D mapping of a scene. The goal of this project is to provide a real-time, accurate, and intuitive representation of the spatial relationships between objects in a given scene. 
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Deployment](#deployment)
- [Usage](#usage)
- [Built Using](#built_using)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)

## 🧐 About <a name = "about"></a>

This project leverages PyTorch's MiDaS model and Open3D's point cloud implementation to attempt an orthogonal 3D mapping of a scene.

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites

The project build is tested on Python 3.9 and 3.10. For Mac and Linux environments, it is recommended that you manage your versions with [pyenv](https://github.com/pyenv/pyenv), or (for the general case) use a [virtual env](https://docs.python.org/3/library/venv.html) to avoid clashing dependencies with Torch packages.

### Installing

A step by step series of examples that tell you how to get a development env running.

First, you need to install the Python requirements.

```bash
pip install -r requirements.txt
```

## 🚀 Deployment <a name = "deployment"></a>

To run the model on an image, replace `FILENAME` with the file name (with path and extension) of the image to be used as input. For the `--level` configuration option, input an integer 1-3, 1 being the lowest accuracy with highest inference speed and 3 being highest accuracy with slowest inference speed.

```bash
python3 main.py --level [1|2|3] --image FILENAME
```

## ⛏️ Built Using <a name = "built_using"></a>

- [PyTorch](https://pytorch.org/)
- [Open3D](https://open3d.org/)

## ✍️ Authors <a name = "authors"></a>

- [@jgfranco17](https://github.com/jgfranco17)

## 🎉 Acknowledgements <a name = "acknowledgement"></a>

- Hat tip to anyone whose code was used
- Inspiration
- References
